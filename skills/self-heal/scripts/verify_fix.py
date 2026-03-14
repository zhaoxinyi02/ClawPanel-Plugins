#!/usr/bin/env python3
"""
Self-Heal Verify Fix Script
Verifies that applied fixes actually resolved the issues.
"""

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

def get_tool_path(tool_name):
    """Get the full path of a tool."""
    result = subprocess.run(
        ["which", tool_name],
        capture_output=True,
        timeout=5
    )
    if result.returncode == 0:
        return result.stdout.decode().strip()
    return None

def run_command_with_check(cmd, description, check_func=None):
    """Run a command and optionally verify with a check function."""
    print(f"   Running: {description}...")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"   ✅ Success")

            if check_func:
                return check_func(result.stdout, result.stderr)

            return True
        else:
            print(f"   ❌ Failed: {result.stderr.decode()[:100]}")
            return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def verify_tool_fix(tool_name):
    """Verify a tool fix worked."""
    print(f"🛠 Verifying tool fix: {tool_name}")

    def check(output, error):
        return get_tool_path(tool_name) is not None

    return run_command_with_check(
        ["which", tool_name],
        f"Checking {tool_name} availability",
        check
    )

def verify_process_fix(process_name):
    """Verify a process is running."""
    print(f"📊 Verifying process: {process_name}")

    def check(output, error):
        lines = output.decode().split("\n")
        for line in lines:
            if process_name in line.lower() and "grep" not in line:
                return True
        return False

    return run_command_with_check(
        ["ps", "aux"],
        f"Checking {process_name} process",
        check
    )

def verify_config_fix(config_path):
    """Verify a config file is valid."""
    print(f"⚙️ Verifying config: {config_path}")

    path = Path(config_path)

    if not path.exists():
        print(f"   ❌ File not found")
        return False

    try:
        if path.suffix == ".json":
            import json
            with open(path, 'r') as f:
                json.load(f)
            print(f"   ✅ JSON is valid")
            return True
        elif path.suffix in [".yaml", ".yml"]:
            with open(path, 'r') as f:
                content = f.read()
            if content.strip():
                print(f"   ✅ YAML file exists and has content")
                return True
    except Exception as e:
        print(f"   ❌ Validation error: {e}")
        return False

    return True

def verify_dependency_fix(package_name):
    """Verify a dependency is installed and importable."""
    print(f"📦 Verifying dependency: {package_name}")

    try:
        result = subprocess.run(
            [sys.executable, "-c", f"import {package_name}"],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"   ✅ Package is importable")
            return True
        print(f"   ❌ Package not importable")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def run_retry_test(issue_type, original_issue):
    """Run a test to verify the original issue is resolved."""
    print(f"🔄 Running retry test for: {issue_type}")

    # Simple retry logic based on issue type
    if issue_type == "tool_failure":
        tool = original_issue.get("tool")
        if tool:
            return verify_tool_fix(tool)

    elif issue_type == "process_crash":
        process = original_issue.get("process")
        if process:
            return verify_process_fix(process)

    elif issue_type == "config_error":
        config = original_issue.get("file")
        if config:
            return verify_config_fix(config)

    elif issue_type == "dependency_missing":
        package = original_issue.get("package")
        if package:
            return verify_dependency_fix(package)

    print(f"   ⚠️ No specific verification for this issue type")
    return True

def verify_fix(issue_id, issue_type, original_issue):
    """
    Main function to verify a fix.

    Args:
        issue_id: ID of the issue being verified
        issue_type: Type of issue (tool_failure, process_crash, config_error, dependency_missing)
        original_issue: Dict with original issue details

    Returns:
        dict: Verification result
    """
    print()
    print("=" * 50)
    print(f"🔍 Verifying Fix")
    print(f"   Issue ID: {issue_id}")
    print(f"   Issue Type: {issue_type}")
    print("=" * 50)

    result = {
        "issue_id": issue_id,
        "issue_type": issue_type,
        "original_issue": original_issue,
        "checks": [],
        "verified": False,
        "timestamp": datetime.now().isoformat()
    }

    # Run verification checks
    checks = []

    # Check 1: Run retry test
    print()
    print("Check 1: Running retry test...")
    retry_ok = run_retry_test(issue_type, original_issue)
    checks.append({
        "name": "retry_test",
        "passed": retry_ok
    })

    # Check 2: Verify tool/process/config/dependency based on type
    if issue_type == "tool_failure" and original_issue.get("tool"):
        print()
        print("Check 2: Tool-specific verification...")
        tool_ok = verify_tool_fix(original_issue["tool"])
        checks.append({
            "name": "tool_verification",
            "passed": tool_ok
        })

    elif issue_type == "process_crash" and original_issue.get("process"):
        print()
        print("Check 2: Process-specific verification...")
        process_ok = verify_process_fix(original_issue["process"])
        checks.append({
            "name": "process_verification",
            "passed": process_ok
        })

    elif issue_type == "config_error" and original_issue.get("file"):
        print()
        print("Check 2: Config-specific verification...")
        config_ok = verify_config_fix(original_issue["file"])
        checks.append({
            "name": "config_verification",
            "passed": config_ok
        })

    elif issue_type == "dependency_missing" and original_issue.get("package"):
        print()
        print("Check 2: Dependency-specific verification...")
        dep_ok = verify_dependency_fix(original_issue["package"])
        checks.append({
            "name": "dependency_verification",
            "passed": dep_ok
        })

    # Determine overall verification status
    result["checks"] = checks
    result["verified"] = all(check["passed"] for check in checks)

    # Summary
    print()
    print("=" * 50)
    print(f"📊 Verification Result: {'✅ PASSED' if result['verified'] else '❌ FAILED'}")
    for check in checks:
        status = "✅" if check["passed"] else "❌"
        print(f"   {status} {check['name']}")
    print("=" * 50)

    return result

def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Verify fix")
    parser.add_argument("--issue-id", required=True, help="ID of the issue")
    parser.add_argument("--issue-type", required=True,
                        choices=["tool_failure", "process_crash", "config_error", "dependency_missing"],
                        help="Type of issue")
    parser.add_argument("--issue", help="Original issue JSON string")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    original_issue = {}
    if args.issue:
        try:
            original_issue = json.loads(args.issue)
        except Exception:
            pass

    result = verify_fix(args.issue_id, args.issue_type, original_issue)

    if args.json:
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["verified"] else 1

if __name__ == "__main__":
    sys.exit(main())

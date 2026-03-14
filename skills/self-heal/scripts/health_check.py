#!/usr/bin/env python3
"""
Self-Heal Health Check Script
Detects tool failures, process issues, config errors, and dependency problems.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = ROOT_DIR = Path(__file__).parent.parent.parent.parent
WORKSPACE_DIR = ROOT_DIR
LOG_DIR = WORKSPACE_DIR / "logs"
STATE_DIR = WORKSPACE_DIR / "state"

def get_recent_errors(hours=1):
    """Get recent errors from logs."""
    errors = []
    cutoff = datetime.now() - timedelta(hours=hours)

    if LOG_DIR.exists():
        for log_file in LOG_DIR.glob("*.log"):
            try:
                with open(log_file, 'r') as f:
                    for line in f:
                        if "error" in line.lower() or "failed" in line.lower():
                            # Try to parse timestamp
                            parts = line.split("] ")
                            if len(parts) >= 2:
                                # Simplified timestamp parsing
                                errors.append({
                                    "source": log_file.name,
                                    "message": line.strip()[:200]
                                })
            except Exception:
                pass

    return errors[-10:]  # Last 10 errors

def check_tool_availability():
    """Check if required tools are available."""
    required_tools = ["python3", "git", "bash", "curl"]
    available = []
    unavailable = []

    for tool in required_tools:
        result = subprocess.run(
            ["which", tool],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            available.append(tool)
        else:
            unavailable.append(tool)

    return available, unavailable

def check_processes():
    """Check for running OpenClaw processes."""
    processes = []

    try:
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            timeout=10
        )
        for line in result.stdout.decode().split("\n"):
            if "openclaw" in line.lower() or "claw" in line.lower():
                if "grep" not in line:
                    processes.append(line.strip()[:100])
    except Exception as e:
        pass

    return processes

def check_config():
    """Check configuration validity."""
    config_issues = []

    # Check main config
    config_paths = [
        ROOT_DIR / "config.yaml",
        ROOT_DIR / "config.json",
        ROOT_DIR / ".env"
    ]

    for config_path in config_paths:
        if config_path.exists():
            try:
                if config_path.suffix == ".json":
                    import json
                    with open(config_path) as f:
                        json.load(f)
            except json.JSONDecodeError as e:
                config_issues.append({
                    "file": str(config_path),
                    "error": f"JSON parse error: {e}"
                })
            except Exception as e:
                config_issues.append({
                    "file": str(config_path),
                    "error": str(e)[:100]
                })

    return config_issues

def check_dependencies():
    """Check if critical dependencies are available."""
    deps = []

    # Check Python packages
    critical_packages = ["requests", "pyyaml", "json"]

    for pkg in critical_packages:
        result = subprocess.run(
            [sys.executable, "-c", f"import {pkg}"],
            capture_output=True,
            timeout=5
        )
        status = "ok" if result.returncode == 0 else "missing"
        deps.append({"package": pkg, "status": status})

    return deps

def check_skill_files():
    """Check if skill files are accessible."""
    skills_dir = ROOT_DIR / "skills"
    issues = []

    if skills_dir.exists():
        for skill in skills_dir.iterdir():
            if skill.is_dir():
                skill_md = skill / "SKILL.md"
                if not skill_md.exists():
                    issues.append({
                        "skill": skill.name,
                        "error": "SKILL.md missing"
                    })

    return issues

def calculate_health_score(issues):
    """Calculate a simple health score (0-100)."""
    base_score = 100

    # Deduct for critical issues
    critical_deduct = len([i for i in issues if i.get("severity") == "critical"]) * 20
    high_deduct = len([i for i in issues if i.get("severity") == "high"]) * 10
    medium_deduct = len([i for i in issues if i.get("severity") == "medium"]) * 5
    low_deduct = len([i for i in issues if i.get("severity") == "low"]) * 2

    return max(0, base_score - critical_deduct - high_deduct - medium_deduct - low_deduct)

def run_health_check():
    """Run complete health check."""
    all_issues = []

    print("🔍 Running health check...")
    print()

    # Get recent errors
    print("📋 Checking recent errors...")
    recent_errors = get_recent_errors()
    if recent_errors:
        for err in recent_errors:
            all_issues.append({
                "type": "recent_error",
                "source": err["source"],
                "message": err["message"],
                "severity": "medium"
            })
            print(f"   ⚠️ {err['source']}: {err['message'][:50]}...")
    else:
        print("   ✅ No recent errors found")

    # Check tools
    print()
    print("🛠 Checking tool availability...")
    available, unavailable = check_tool_availability()
    for tool in unavailable:
        all_issues.append({
            "type": "tool_unavailable",
            "tool": tool,
            "severity": "high"
        })
        print(f"   ⚠️ Tool unavailable: {tool}")

    # Check processes
    print()
    print("📊 Checking processes...")
    processes = check_processes()
    if len(processes) <= 1:  # Only grep or empty
        print("   ⚠️ No OpenClaw processes detected")
    else:
        print(f"   ✅ {len(processes)} processes running")

    # Check config
    print()
    print("⚙️ Checking configuration...")
    config_issues = check_config()
    for issue in config_issues:
        all_issues.append({
            "type": "config_error",
            "file": issue["file"],
            "error": issue["error"],
            "severity": "high"
        })
        print(f"   ⚠️ Config error in {issue['file']}: {issue['error'][:50]}")

    # Check dependencies
    print()
    print("📦 Checking dependencies...")
    deps = check_dependencies()
    for dep in deps:
        status = "✅" if dep["status"] == "ok" else "❌"
        print(f"   {status} {dep['package']}: {dep['status']}")
        if dep["status"] == "missing":
            all_issues.append({
                "type": "dependency_missing",
                "package": dep["package"],
                "severity": "high"
            })

    # Check skills
    print()
    print("🎯 Checking skill files...")
    skill_issues = check_skill_files()
    for issue in skill_issues:
        all_issues.append({
            "type": "skill_missing",
            "skill": issue["skill"],
            "error": issue["error"],
            "severity": "low"
        })
        print(f"   ⚠️ {issue['skill']}: {issue['error']}")

    # Calculate health score
    health_score = calculate_health_score(all_issues)

    print()
    print("=" * 50)
    print(f"🏥 Health Score: {health_score}/100")
    print(f"📊 Issues Found: {len(all_issues)}")
    print("=" * 50)

    # Output JSON for programmatic use
    result = {
        "timestamp": datetime.now().isoformat(),
        "health_score": health_score,
        "issues": all_issues,
        "summary": {
            "critical": len([i for i in all_issues if i.get("severity") == "critical"]),
            "high": len([i for i in all_issues if i.get("severity") == "high"]),
            "medium": len([i for i in all_issues if i.get("severity") == "medium"]),
            "low": len([i for i in all_issues if i.get("severity") == "low"])
        }
    }

    print()
    print("📄 JSON Output:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    return result

if __name__ == "__main__":
    try:
        result = run_health_check()
        sys.exit(0 if result["health_score"] >= 80 else 1)
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        sys.exit(2)

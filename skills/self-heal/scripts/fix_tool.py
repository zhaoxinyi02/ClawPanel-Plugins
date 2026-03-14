#!/usr/bin/env python3
"""
Self-Heal Fix Tool Script
Attempts to fix tool-related issues (missing tools, permission errors, path problems).
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime

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

def fix_missing_package(tool_name):
    """Try to install a missing package."""
    print(f"📦 Attempting to install {tool_name}...")

    # Try apt (Debian/Ubuntu)
    if shutil.which("apt-get"):
        result = subprocess.run(
            ["sudo", "apt-get", "install", "-y", tool_name],
            capture_output=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"   ✅ Installed {tool_name} via apt")
            return True

    # Try pip (Python packages)
    if tool_name in ["requests", "pyyaml", "json", "python-dateutil"]:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", tool_name],
            capture_output=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"   ✅ Installed {tool_name} via pip")
            return True

    print(f"   ❌ Could not install {tool_name}")
    return False

def fix_permission_error(tool_path):
    """Fix permission errors for a tool."""
    print(f"🔧 Checking permissions for {tool_path}...")

    try:
        # Check if file exists
        if not os.path.exists(tool_path):
            print(f"   ⚠️ File does not exist: {tool_path}")
            return False

        # Get current permissions
        current_mode = os.stat(tool_path).st_mode & 0o777
        print(f"   Current permissions: {oct(current_mode)}")

        # Try to add execute permission
        new_mode = current_mode | 0o111
        os.chmod(tool_path, new_mode)
        print(f"   ✅ Updated permissions to {oct(new_mode)}")

        return True

    except Exception as e:
        print(f"   ❌ Could not fix permissions: {e}")
        return False

def fix_path_issue(tool_name):
    """Fix PATH-related issues by finding or creating symlinks."""
    print(f"🔍 Checking PATH configuration...")

    # Common locations to search
    common_paths = [
        "/usr/bin",
        "/usr/local/bin",
        "/home/node/.local/bin",
        "/opt/homebrew/bin",
    ]

    for path in common_paths:
        full_path = Path(path) / tool_name
        if full_path.exists():
            print(f"   ✅ Found at: {full_path}")
            return True

    print(f"   ⚠️ {tool_name} not found in common locations")
    return False

def retry_tool_execution(tool_name, args=None, max_retries=3):
    """Retry executing a tool with exponential backoff."""
    print(f"🔄 Retrying {tool_name}...")

    import time

    for attempt in range(1, max_retries + 1):
        wait_time = 2 ** attempt  # Exponential backoff
        print(f"   Attempt {attempt}/{max_retries} (waiting {wait_time}s)...")
        time.sleep(wait_time)

        try:
            cmd = [tool_name]
            if args:
                cmd.extend(args)

            result = subprocess.run(
                cmd,
                capture_output=True,
                timeout=30
            )

            if result.returncode == 0:
                print(f"   ✅ Success on attempt {attempt}")
                return True

            print(f"   ❌ Failed: {result.stderr.decode()[:100]}")

        except Exception as e:
            print(f"   ❌ Error: {e}")

    print(f"   ⚠️ All {max_retries} attempts failed")
    return False

def create_fallback_handler(tool_name, error_msg):
    """Create a fallback handler when tool cannot be fixed."""
    print(f"🛡️ Creating fallback handler for {tool_name}...")

    fallback_script = Path(__file__).parent / "fallbacks" / f"{tool_name}_fallback.py"
    fallback_script.parent.mkdir(exist_ok=True)

    fallback_code = f'''#!/usr/bin/env python3
"""
Fallback handler for {tool_name}
Created by self-heal when the primary tool is unavailable.
"""

import subprocess
import sys

def run():
    """Fallback execution."""
    print("⚠️ Using fallback handler for {tool_name}")
    print(f"Original error: {error_msg}")

    # Alternative approaches can be added here
    # For now, just return an error
    sys.exit(1)

if __name__ == "__main__":
    run()
'''

    try:
        with open(fallback_script, 'w') as f:
            f.write(fallback_code)
        os.chmod(fallback_script, 0o755)
        print(f"   ✅ Fallback created: {fallback_script}")
        return str(fallback_script)
    except Exception as e:
        print(f"   ❌ Could not create fallback: {e}")
        return None

def fix_tool(tool_name, error_msg=None):
    """
    Main function to fix a tool-related issue.

    Args:
        tool_name: Name of the tool with issues
        error_msg: Error message from the failure

    Returns:
        dict: Fix result with success status and details
    """
    print()
    print("=" * 50)
    print(f"🔧 Fixing tool: {tool_name}")
    print(f"   Error: {error_msg or 'Unknown error'}")
    print("=" * 50)

    result = {
        "tool": tool_name,
        "error": error_msg,
        "attempts": [],
        "success": False,
        "fallback_created": False
    }

    # Step 1: Check if tool exists
    print()
    print("Step 1: Checking if tool exists...")
    tool_path = get_tool_path(tool_name)

    if tool_path:
        print(f"   ✅ Tool found at: {tool_path}")
    else:
        print(f"   ⚠️ Tool not found")

        # Step 1a: Try to install
        print()
        print("Step 2: Attempting to install...")
        if fix_missing_package(tool_name):
            result["attempts"].append({
                "action": "install_package",
                "success": True
            })

            # Verify installation
            if get_tool_path(tool_name):
                result["success"] = True
        else:
            result["attempts"].append({
                "action": "install_package",
                "success": False
            })

    # Step 2: If tool exists but had issues, check permissions
    if tool_path and error_msg:
        if "permission" in error_msg.lower():
            print()
            print("Step 3: Fixing permissions...")
            if fix_permission_error(tool_path):
                result["attempts"].append({
                    "action": "fix_permissions",
                    "success": True
                })
                result["success"] = True

    # Step 3: If still not working, try retry
    if not result["success"]:
        print()
        print("Step 4: Attempting retry with backoff...")
        if retry_tool_execution(tool_name):
            result["success"] = True
            result["attempts"].append({
                "action": "retry",
                "success": True
            })

    # Step 4: If all else fails, create fallback
    if not result["success"]:
        print()
        print("Step 5: Creating fallback handler...")
        fallback = create_fallback_handler(tool_name, error_msg)
        if fallback:
            result["fallback_created"] = True
            result["fallback_path"] = fallback
            result["attempts"].append({
                "action": "create_fallback",
                "success": True
            })

    # Summary
    print()
    print("=" * 50)
    print(f"📊 Fix Result: {'✅ SUCCESS' if result['success'] else '❌ FAILED'}")
    if result["success"]:
        print(f"   Tool {tool_name} should now be functional")
    else:
        print(f"   Could not fix {tool_name}")
        if result["fallback_created"]:
            print(f"   Fallback created at: {result.get('fallback_path')}")
    print("=" * 50)

    return result

def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix tool-related issues")
    parser.add_argument("--tool", required=True, help="Name of the tool to fix")
    parser.add_argument("--error", help="Error message from the failure")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    result = fix_tool(args.tool, args.error)

    if args.json:
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["success"] or result["fallback_created"] else 1

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Self-Heal Fix Dependency Script
Installs or verifies required dependencies.
"""

import json
import subprocess
import sys
from pathlib import Path

def check_package_installed(package_name):
    """Check if a package is installed."""
    try:
        # Try pip first
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            return True, "pip"

        # Try apt
        result = subprocess.run(
            ["dpkg", "-l", package_name],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            return True, "apt"

    except Exception:
        pass

    return False, None

def install_via_pip(package_name):
    """Install package via pip."""
    print(f"   Installing {package_name} via pip...")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name, "--quiet"],
            capture_output=True,
            timeout=120
        )

        if result.returncode == 0:
            print(f"   ✅ Installed {package_name}")
            return True

        # Try with user flag
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", package_name],
            capture_output=True,
            timeout=120
        )

        if result.returncode == 0:
            print(f"   ✅ Installed {package_name} (--user)")
            return True

        print(f"   ❌ pip install failed")
        return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def install_via_apt(package_name):
    """Install package via apt."""
    print(f"   Installing {package_name} via apt...")

    try:
        result = subprocess.run(
            ["sudo", "apt-get", "install", "-y", package_name],
            capture_output=True,
            timeout=120
        )

        if result.returncode == 0:
            print(f"   ✅ Installed {package_name}")
            return True

        print(f"   ❌ apt install failed")
        return False

    except FileNotFoundError:
        print("   ⚠️ apt-get not available")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def install_package(package_name):
    """Try to install a package using available methods."""
    print(f"📦 Installing {package_name}...")

    # Check if already installed
    installed, source = check_package_installed(package_name)
    if installed:
        print(f"   ✅ {package_name} already installed ({source})")
        return True

    # Try pip first for Python packages
    if package_name in ["requests", "pyyaml", "json", "python-dateutil", "aiohttp", "websockets"]:
        if install_via_pip(package_name):
            return True

    # Try apt for system packages
    if install_via_apt(package_name):
        return True

    return False

def verify_installation(package_name):
    """Verify a package is working."""
    try:
        result = subprocess.run(
            [sys.executable, "-c", f"import {package_name}"],
            capture_output=True,
            timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False

def fix_dependency(package_name, error_msg=None):
    """
    Main function to fix a dependency issue.

    Args:
        package_name: Name of the missing package
        error_msg: Error message from the failure

    Returns:
        dict: Fix result
    """
    print()
    print("=" * 50)
    print(f"🔧 Fixing Dependency: {package_name}")
    if error_msg:
        print(f"   Error: {error_msg}")
    print("=" * 50)

    result = {
        "package": package_name,
        "error": error_msg,
        "attempts": [],
        "success": False
    }

    # Step 1: Check if already installed
    print()
    print("Step 1: Checking if installed...")
    installed, source = check_package_installed(package_name)

    if installed:
        print(f"   ✅ {package_name} already installed ({source})")
        result["success"] = True
        result["attempts"].append({
            "action": "check",
            "success": True,
            "source": source
        })
        return result

    # Step 2: Try to install
    print()
    print("Step 2: Attempting installation...")

    if install_package(package_name):
        result["success"] = True
        result["attempts"].append({
            "action": "install",
            "success": True
        })
    else:
        result["attempts"].append({
            "action": "install",
            "success": False
        })

    # Step 3: Verify
    if result["success"]:
        print()
        print("Step 3: Verifying installation...")
        if verify_installation(package_name):
            print(f"   ✅ {package_name} is working")
        else:
            print(f"   ⚠️ {package_name} installed but not importable")
            result["success"] = False
            result["attempts"].append({
                "action": "verify",
                "success": False
            })

    # Summary
    print()
    print("=" * 50)
    print(f"📊 Fix Result: {'✅ SUCCESS' if result['success'] else '❌ FAILED'}")
    print("=" * 50)

    return result

def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix dependency issues")
    parser.add_argument("--package", required=True, help="Package name to install")
    parser.add_argument("--error", help="Error message from the failure")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    result = fix_dependency(args.package, args.error)

    if args.json:
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["success"] else 1

if __name__ == "__main__":
    sys.exit(main())

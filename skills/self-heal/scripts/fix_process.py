#!/usr/bin/env python3
"""
Self-Heal Fix Process Script
Recovers crashed or hung processes.
"""

import json
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

def get_process_info(pid):
    """Get information about a process by PID."""
    try:
        result = subprocess.run(
            ["ps", "-p", str(pid), "-o", "pid,ppid,stat,time,cmd"],
            capture_output=True,
            timeout=10
        )
        lines = result.stdout.decode().strip().split("\n")
        if len(lines) > 1:
            parts = lines[1].split()
            return {
                "pid": parts[0] if parts else None,
                "ppid": parts[1] if len(parts) > 1 else None,
                "stat": parts[2] if len(parts) > 2 else None,
                "cmd": " ".join(parts[4:]) if len(parts) > 4 else None
            }
    except Exception:
        pass
    return None

def find_openclaw_processes():
    """Find all OpenClaw related processes."""
    processes = []

    try:
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            timeout=10
        )
        for line in result.stdout.decode().split("\n"):
            if "openclaw" in line.lower() or "claw" in line.lower():
                if "grep" not in line and "python" not in line.lower():
                    parts = line.split()
                    if len(parts) >= 2:
                        try:
                            pid = int(parts[1])
                            processes.append({
                                "pid": pid,
                                "raw": line.strip()
                            })
                        except ValueError:
                            pass
    except Exception as e:
        print(f"Error finding processes: {e}")

    return processes

def get_child_pids(parent_pid):
    """Get all child PIDs of a parent process."""
    children = []

    try:
        result = subprocess.run(
            ["pgrep", "-P", str(parent_pid)],
            capture_output=True,
            timeout=10
        )
        for line in result.stdout.decode().strip().split("\n"):
            if line.strip():
                try:
                    children.append(int(line.strip()))
                except ValueError:
                    pass
    except Exception:
        pass

    return children

def terminate_process(pid, timeout=5):
    """Gracefully terminate a process."""
    try:
        # First try SIGTERM
        os.kill(pid, signal.SIGTERM)
        print(f"   Sent SIGTERM to PID {pid}")

        # Wait for graceful shutdown
        for _ in range(timeout * 10):
            try:
                os.kill(pid, 0)  # Check if still running
                time.sleep(0.1)
            except OSError:
                print(f"   Process {pid} terminated gracefully")
                return True

        # Force kill if still running
        os.kill(pid, signal.SIGKILL)
        print(f"   Force killed PID {pid}")
        return True

    except ProcessLookupError:
        print(f"   Process {pid} already terminated")
        return True
    except Exception as e:
        print(f"   Error terminating {pid}: {e}")
        return False

def restart_openclaw():
    """Restart the OpenClaw service."""
    print("🔄 Attempting to restart OpenClaw...")

    # Try different restart methods
    methods = [
        ("systemctl", ["systemctl", "restart", "openclaw"]),
        ("service", ["service", "openclaw", "restart"]),
        ("docker", ["docker", "restart", "openclaw"]),
        ("direct", [sys.executable, "-m", "openclaw"]),  # Fallback
    ]

    for method_name, cmd in methods:
        try:
            print(f"   Trying {method_name}...")
            result = subprocess.run(
                cmd,
                capture_output=True,
                timeout=30
            )

            if result.returncode == 0:
                print(f"   ✅ OpenClaw restarted via {method_name}")
                return True

            print(f"   ❌ {method_name} failed: {result.stderr.decode()[:100]}")

        except FileNotFoundError:
            print(f"   ⚠️ {method_name} not available")
        except Exception as e:
            print(f"   ❌ {method_name} error: {e}")

    print("   ⚠️ Could not restart OpenClaw automatically")
    return False

def wait_for_service(timeout=30):
    """Wait for OpenClaw to become responsive."""
    print(f"⏳ Waiting for OpenClaw (timeout: {timeout}s)...")

    for i in range(timeout):
        try:
            # Try a simple check
            result = subprocess.run(
                ["curl", "-s", "http://localhost:8080/health"],
                capture_output=True,
                timeout=2
            )
            if result.returncode == 0:
                print("   ✅ OpenClaw is responsive")
                return True
        except Exception:
            pass

        time.sleep(1)

    print("   ⚠️ OpenClaw did not respond in time")
    return False

def check_process_health():
    """Check if OpenClaw processes are healthy."""
    processes = find_openclaw_processes()

    if not processes:
        return {
            "healthy": False,
            "reason": "No OpenClaw processes found",
            "process_count": 0
        }

    # Check if main process is running
    main_running = any(
        "openclaw" in p["raw"].lower() and "python" not in p["raw"].lower()
        for p in processes
    )

    return {
        "healthy": main_running,
        "process_count": len(processes),
        "processes": processes
    }

def fix_process(process_name=None, pid=None):
    """
    Main function to fix process issues.

    Args:
        process_name: Name of the process to fix
        pid: Specific PID to fix

    Returns:
        dict: Fix result
    """
    print()
    print("=" * 50)
    print("🔧 Fixing Process")
    print("=" * 50)

    result = {
        "action": "fix_process",
        "process_name": process_name,
        "pid": pid,
        "steps": [],
        "success": False
    }

    # Step 1: Check current health
    print()
    print("Step 1: Checking process health...")
    health = check_process_health()
    print(f"   Health: {'✅ OK' if health['healthy'] else '❌ UNHEALTHY'}")
    print(f"   Processes: {health.get('process_count', 0)}")

    if health["healthy"]:
        result["success"] = True
        result["message"] = "Process already healthy"
        return result

    result["steps"].append({
        "step": "health_check",
        "healthy": False
    })

    # Step 2: If specified PID, check if it's running
    if pid:
        print()
        print(f"Step 2: Checking specified PID {pid}...")
        proc_info = get_process_info(pid)

        if proc_info:
            print(f"   PID {pid}: {proc_info}")

            # Get children
            children = get_child_pids(pid)
            print(f"   Children: {children}")

            # Terminate process tree
            print()
            print("Step 3: Terminating process...")
            for child_pid in children:
                terminate_process(child_pid)

            if terminate_process(pid):
                result["steps"].append({
                    "step": "terminate",
                    "success": True
                })
        else:
            print(f"   Process {pid} not found")
            result["steps"].append({
                "step": "terminate",
                "message": "Process already gone"
            })

    # Step 3: Restart service
    print()
    print("Step 4: Restarting OpenClaw...")
    if restart_openclaw():
        result["steps"].append({
            "step": "restart",
            "success": True
        })

        # Step 4: Wait for service
        print()
        print("Step 5: Waiting for service...")
        if wait_for_service():
            result["success"] = True
            result["steps"].append({
                "step": "wait_for_service",
                "success": True
            })
    else:
        result["steps"].append({
            "step": "restart",
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

    parser = argparse.ArgumentParser(description="Fix process issues")
    parser.add_argument("--process", help="Process name to fix")
    parser.add_argument("--pid", type=int, help="Specific PID to fix")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    result = fix_process(process_name=args.process, pid=args.pid)

    if args.json:
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["success"] else 1

if __name__ == "__main__":
    sys.exit(main())

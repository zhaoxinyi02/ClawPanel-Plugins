#!/usr/bin/env python3
"""
Self-Heal Evolve Script
Records successful fixes to build a knowledge base for future improvements.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
KB_FILE = SCRIPT_DIR / "knowledge_base.json"

# Knowledge base structure
KB_TEMPLATE = {
    "version": "1.0",
    "last_updated": None,
    "stats": {
        "total_fixes": 0,
        "successful_fixes": 0,
        "fix_types": {}
    },
    "patterns": {
        "tool_failure": [],
        "process_crash": [],
        "config_error": [],
        "dependency_missing": []
    }
}

def load_knowledge_base():
    """Load the knowledge base from file."""
    if KB_FILE.exists():
        try:
            with open(KB_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Could not load knowledge base: {e}")

    return KB_TEMPLATE.copy()

def save_knowledge_base(kb):
    """Save the knowledge base to file."""
    try:
        kb["last_updated"] = datetime.now().isoformat()
        with open(KB_FILE, 'w') as f:
            json.dump(kb, f, indent=2, ensure_ascii=False)
        print(f"   ✅ Knowledge base saved")
        return True
    except Exception as e:
        print(f"   ❌ Could not save knowledge base: {e}")
        return False

def record_fix_pattern(kb, issue_type, error_sig, fix_applied, outcome):
    """Record a fix pattern in the knowledge base."""
    pattern = {
        "error_signature": error_sig,
        "fix_applied": fix_applied,
        "outcome": outcome,
        "timestamp": datetime.now().isoformat(),
        "success_count": 1 if outcome == "success" else 0
    }

    if issue_type in kb["patterns"]:
        # Check if similar pattern exists
        existing = None
        for p in kb["patterns"][issue_type]:
            if p["error_signature"] == error_sig:
                existing = p
                break

        if existing:
            # Update existing pattern
            existing["fix_applied"] = fix_applied
            existing["success_count"] += 1 if outcome == "success" else 0
            existing["last_attempt"] = datetime.now().isoformat()
            print(f"   📝 Updated pattern: {error_sig[:50]}...")
        else:
            # Add new pattern
            kb["patterns"][issue_type].append(pattern)
            print(f"   📝 New pattern recorded: {error_sig[:50]}...")

    # Update stats
    kb["stats"]["total_fixes"] += 1
    if outcome == "success":
        kb["stats"]["successful_fixes"] += 1

    if issue_type not in kb["stats"]["fix_types"]:
        kb["stats"]["fix_types"][issue_type] = 0
    kb["stats"]["fix_types"][issue_type] += 1

def get_common_fixes(issue_type, error_sig):
    """Get common fixes for a similar error from knowledge base."""
    kb = load_knowledge_base()

    if issue_type not in kb["patterns"]:
        return []

    similar = []
    for pattern in kb["patterns"][issue_type]:
        # Check if error signature is similar
        if error_sig and pattern["error_signature"]:
            if error_sig[:30] in pattern["error_signature"] or \
               pattern["error_signature"][:30] in error_sig:
                if pattern.get("success_count", 0) > 0:
                    similar.append({
                        "fix": pattern["fix_applied"],
                        "success_count": pattern["success_count"]
                    })

    # Sort by success count
    similar.sort(key=lambda x: x["success_count"], reverse=True)
    return similar[:5]  # Top 5 fixes

def suggest_fixes(issue_type, error_sig):
    """Suggest fixes based on historical patterns."""
    suggestions = get_common_fixes(issue_type, error_sig)

    if suggestions:
        print(f"\n💡 Historical fixes that worked:")
        for i, s in enumerate(suggestions, 1):
            print(f"   {i}. {s['fix']} (used {s['success_count']} times)")

    return suggestions

def evolve(issue_type, fix_applied, outcome, error_sig=None):
    """
    Main function to record and learn from fixes.

    Args:
        issue_type: Type of issue (tool_failure, process_crash, etc.)
        fix_applied: Description of the fix that was applied
        outcome: Result of the fix (success, partial, failed)
        error_sig: Signature of the error for pattern matching

    Returns:
        dict: Evolution result
    """
    print()
    print("=" * 50)
    print(f"🧬 Evolving: {issue_type}")
    print(f"   Fix: {fix_applied}")
    print(f"   Outcome: {outcome}")
    print("=" * 50)

    result = {
        "issue_type": issue_type,
        "fix_applied": fix_applied,
        "outcome": outcome,
        "error_signature": error_sig,
        "recorded": False,
        "suggestions": []
    }

    # Load knowledge base
    kb = load_knowledge_base()

    # Record the fix pattern
    record_fix_pattern(kb, issue_type, error_sig or "", fix_applied, outcome)

    # Save updated knowledge base
    if save_knowledge_base(kb):
        result["recorded"] = True

    # Suggest improvements based on history
    if error_sig:
        suggestions = suggest_fixes(issue_type, error_sig)
        result["suggestions"] = suggestions

    # Summary
    print()
    print("=" * 50)
    print(f"📊 Evolution Result: {'✅ RECORDED' if result['recorded'] else '❌ FAILED'}")
    print("=" * 50)

    return result

def show_knowledge_base():
    """Display the current knowledge base stats."""
    kb = load_knowledge_base()

    print()
    print("🧠 Knowledge Base Stats")
    print("=" * 50)
    print(f"Version: {kb.get('version', 'unknown')}")
    print(f"Last Updated: {kb.get('last_updated', 'never')}")
    print(f"Total Fixes: {kb['stats']['total_fixes']}")
    print(f"Successful: {kb['stats']['successful_fixes']}")
    print()

    print("By Type:")
    for issue_type, count in kb["stats"]["fix_types"].items():
        print(f"  • {issue_type}: {count}")

    print()
    print("Patterns by Type:")
    for issue_type, patterns in kb["patterns"].items():
        if patterns:
            print(f"  {issue_type}:")
            for p in patterns[:3]:  # Show first 3
                print(f"    - {p['error_signature'][:40]}: {p['fix_applied']} ({p['success_count']} successes)")

def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Evolve - Learn from fixes")
    parser.add_argument("--issue-type", required=True,
                        choices=["tool_failure", "process_crash", "config_error", "dependency_missing"],
                        help="Type of issue")
    parser.add_argument("--fix", required=True, help="Fix that was applied")
    parser.add_argument("--outcome", required=True,
                        choices=["success", "partial", "failed"],
                        help="Result of the fix")
    parser.add_argument("--error-sig", help="Error signature for pattern matching")
    parser.add_argument("--stats", action="store_true", help="Show knowledge base stats")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    if args.stats:
        show_knowledge_base()
        return 0

    result = evolve(args.issue_type, args.fix, args.outcome, args.error_sig)

    if args.json:
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["recorded"] else 1

if __name__ == "__main__":
    sys.exit(main())

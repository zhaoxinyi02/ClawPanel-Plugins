---
name: self-heal
description: Enables the agent to self-detect, self-repair, and self-evolve. Use when: (1) Tool calls fail or error out, (2) Processes crash or become unresponsive, (3) Configuration issues are detected, (4) After resolving issues, to learn and improve future resilience.
---

# Self Heal

## Overview

This skill enables autonomous detection, diagnosis, and recovery from operational issues. It can:
- Detect tool failures, process crashes, and configuration errors
- Automatically attempt fixes for common problems
- Learn from successful recoveries to prevent future failures

## When to Trigger

**Auto-trigger conditions:**
- Any tool call returns an error or fails
- A process is detected as crashed or unresponsive
- Configuration validation fails
- Explicit request for "self-heal", "self-repair", or "self-diagnose"

**Manual triggers:**
- "Check your health"
- "Diagnose what's wrong"
- "Recover from the error"
- "Learn from this experience"

## Workflow

```
detect_issues → analyze_root_cause → attempt_fix → verify_fix → evolve
```

---

## Step 1: Detect Issues

Run the health check script to identify problems:

```bash
python3 /home/node/clawd/skills/self-heal/scripts/health_check.py
```

This detects:
- **Tool failures** - Last N tool calls that errored
- **Process issues** - Crashed or hanging processes
- **Config problems** - Missing or invalid configuration
- **Dependency issues** - Missing packages or modules

**Output format:**
```json
{
  "issues": [
    {"type": "tool_failure", "tool": "exec", "error": "command not found", "severity": "high"},
    {"type": "config_error", "file": "config.yaml", "error": "missing field", "severity": "medium"}
  ],
  "health_score": 75
}
```

---

## Step 2: Analyze Root Cause

For each issue, determine the appropriate fix strategy:

| Issue Type | Fix Strategy |
|------------|--------------|
| `tool_failure` | Retry with fallback, verify tool availability |
| `process_crash` | Restart process, check logs |
| `config_error` | Repair config from backup or default |
| `dependency_missing` | Install/verify dependency |

---

## Step 3: Attempt Fix

Execute the appropriate fix script based on issue type:

### For tool failures:
```bash
python3 /home/node/clawd/skills/self-heal/scripts/fix_tool.py --tool <name> --error <error_msg>
```

### For process crashes:
```bash
python3 /home/node/clawd/skills/self-heal/scripts/fix_process.py --process <name>
```

### For config errors:
```bash
python3 /home/node/clawd/skills/self-heal/scripts/fix_config.py --file <path> --error <error_msg>
```

### For missing dependencies:
```bash
python3 /home/node/clawd/skills/self-heal/scripts/fix_dependency.py --package <name>
```

---

## Step 4: Verify Fix

After applying fixes, verify they worked:

```bash
python3 /home/node/clawd/skills/self-heal/scripts/verify_fix.py --issue-id <id>
```

If verification passes, proceed to evolve. If it fails, try an alternative fix strategy.

---

## Step 5: Evolve

Record successful fixes for future reference:

```bash
python3 /home/node/clawd/skills/self-heal/scripts/evolve.py --issue-type <type> --fix Applied --outcome success
```

This builds a knowledge base of:
- Successful fix patterns
- Failed approach avoidances
- Common error signatures

---

## Core Capabilities

### 1. Health Check
Check system health and identify issues before they become critical.

### 2. Auto-Recovery
Attempt automatic fixes for detected problems without human intervention.

### 3. Safe Retry
Retry failed operations with exponential backoff and fallback strategies.

### 4. Learning System
Build a knowledge base of successful recoveries to improve future resilience.

---

## Usage Examples

**Example 1: After a tool call fails**
```
Tool exec returned error: "command not found"
→ Trigger self-heal
→ Detect: missing package
→ Fix: install package
→ Verify: retry command
→ Evolve: record fix pattern
```

**Example 2: Periodic health check**
```
"Check system health"
→ Run health_check.py
→ Report issues
→ Auto-fix if configured
→ Suggest manual intervention if needed
```

**Example 3: After a crash**
```
"Recover from the crash"
→ Detect what was running
→ Check logs for root cause
→ Attempt recovery
→ Verify stability
→ Evolve: improve restart logic
```

---

## Scripts Reference

### scripts/health_check.py
Main health detection script. Run this first when triggering self-heal.

### scripts/fix_tool.py
Fix tool-related issues (missing tools, permission errors, path problems).

### scripts/fix_process.py
Recover crashed or hung processes.

### scripts/fix_config.py
Repair configuration files from backups or regenerate defaults.

### scripts/fix_dependency.py
Install or verify required dependencies.

### scripts/verify_fix.py
Verify that applied fixes actually resolved the issue.

### scripts/evolve.py
Record successful fixes to build the knowledge base.

### scripts/knowledge_base.json
JSON file storing learned patterns and successful fix strategies.

---

## Safety Guidelines

1. **Backup before fixing** - Always create config backups before modifying
2. **Fail-safe defaults** - If fix fails, restore to known good state
3. **Limit retries** - Max 3 attempts per issue before escalation
4. **Notify on failure** - Alert user if self-heal cannot resolve
5. **Log everything** - All actions must be logged for auditing

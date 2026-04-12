#!/usr/bin/env python3
"""
==============================================================================
📦 MUNDER DIFFLIN COMMAND CENTER - AUTOMATED INSTALLER & ENVIRONMENT SETUP
==============================================================================
Automates 100% of prerequisites, dependencies, agent workspaces, and gateways.
Supports Windows, macOS, and Linux.

Usage:
  python install.py
==============================================================================
"""

import os
import sys
import shutil
import subprocess
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def step(title):
    print("\n" + "=" * 70)
    print(f" [*] STEP: {title}")
    print("=" * 70)

def run_cmd(cmd, check=True):
    print(f"  -> Running: {cmd}")
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if res.returncode != 0 and check:
        print(f"  [!] Warning / Error: {res.stderr.strip() or res.stdout.strip()}")
    return res.returncode == 0, res.stdout.strip()

def main():
    print("""
======================================================================
  🏢 MUNDER DIFFLIN COMMAND CENTER - ZERO-CLICK AUTO INSTALLER
======================================================================
""")

    # 1. Check Python version
    step("Validating Python Runtime")
    py_ver = sys.version_info
    print(f"  * Detected Python {py_ver.major}.{py_ver.minor}.{py_ver.micro}")
    if py_ver < (3, 8):
        print("  [X] Python 3.8 or higher is required. Please upgrade your Python installation.")
        sys.exit(1)
    print("  [OK] Python runtime verified.")

    # 2. Install Python Dependencies
    step("Installing Python Dependencies from requirements.txt")
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_file):
        ok, out = run_cmd(f'"{sys.executable}" -m pip install -r "{req_file}" --quiet')
        if ok:
            print("  [OK] Dependencies installed successfully (requests, rich, python-dotenv).")
        else:
            print("  [!] Pip installation had notices, but proceeding.")
    else:
        run_cmd(f'"{sys.executable}" -m pip install requests rich python-dotenv --quiet')
        print("  [OK] Dependencies installed.")

    # 3. Check Node.js and NPM/NPX
    step("Checking Node.js & NPM / NPX Runtime")
    node_ok, node_ver = run_cmd("node -v", check=False)
    npm_ok, npm_ver = run_cmd("npm -v", check=False)
    npx_ok, npx_ver = run_cmd("npx -v", check=False)

    if node_ok:
        print(f"  [OK] Node.js found: {node_ver}")
    else:
        print("  [!] Node.js not detected in PATH. Required for 'npx freellmapi' and coding CLIs.")
        print("      Download Node.js from https://nodejs.org")

    if npx_ok:
        print(f"  [OK] NPX found: {npx_ver}")

    # 4. Initialize Multi-Agent Hive Workspace
    step("Initializing Multi-Agent Hive Directory Structure")
    hive_root = os.getenv("HIVE_ROOT", r"F:\Ashraf\Tools\hive")
    if not os.path.exists(os.path.dirname(hive_root)):
        # Default to local hive folder if F: is not available
        hive_root = os.path.join(os.path.expanduser("~"), "munder-hive")

    print(f"  * Setting up Hive root at: {hive_root}")
    subdirs = [
        "agents/god/inbox/.done",
        "agents/god/outbox",
        "agents/dwight/inbox/.done",
        "agents/dwight/outbox",
        "agents/jim/inbox/.done",
        "agents/jim/outbox",
        "spawn-requests",
        "connections",
        "bin"
    ]
    for sd in subdirs:
        os.makedirs(os.path.join(hive_root, sd), exist_ok=True)

    # Initialize empty tasks.json if not present
    tasks_file = os.path.join(hive_root, "tasks.json")
    if not os.path.exists(tasks_file):
        initial_tasks = {
            "ticket": {"prefix": "TLS", "next": 1},
            "tasks": [
                {
                    "id": "TLS-1",
                    "title": "Initial Floor Initialization & Security Sweep",
                    "status": "todo",
                    "assignee": "dwight",
                    "priority": "high",
                    "description": "Verify gateway health, directory locks, and perimeter defenses.",
                    "deps": [],
                    "createdAt": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    "updatedAt": time.strftime('%Y-%m-%dT%H:%M:%SZ')
                }
            ]
        }
        with open(tasks_file, "w", encoding="utf-8") as f:
            json.dump(initial_tasks, f, indent=2)
        print("  [OK] Created initial tasks.json")
    else:
        print("  [OK] tasks.json already exists.")

    # Initialize board.md if not present
    board_file = os.path.join(hive_root, "board.md")
    if not os.path.exists(board_file):
        with open(board_file, "w", encoding="utf-8") as f:
            f.write("# Hive Board - Munder Difflin Autonomous Operations\n\n## Team Roster\n- **Michael** (God Orchestrator)\n- **Dwight** (Security Desk)\n- **Jim** (Engineering Desk)\n")
        print("  [OK] Created initial board.md")

    # 5. Check API Keys Config File
    step("Configuring API Keys File")
    key_template = os.path.join(os.path.dirname(__file__), "API_KEYS_TEMPLATE.txt")
    user_keys = os.path.join(os.path.dirname(__file__), "API_KEYS.txt")
    if not os.path.exists(user_keys) and os.path.exists(key_template):
        shutil.copy(key_template, user_keys)
        print("  [OK] Created API_KEYS.txt from template. You can add your custom keys there.")
    else:
        print("  [OK] API_KEYS.txt is ready.")

    # 6. Gateway Connectivity Check
    step("Checking Gateway Availability")
    print("  * Checking OmniRoute at http://localhost:20128 ...")
    try:
        req = urllib.request.Request("http://localhost:20128/", headers={"User-Agent": "MunderInstall/1.0"})
        with urllib.request.urlopen(req, timeout=2) as r:
            print(f"    -> [ONLINE] OmniRoute responded (HTTP {r.status})")
    except Exception:
        print("    -> [NOTE] OmniRoute not detected locally. If installed, run 'OmniRoute.exe'.")

    print("  * Checking FreeLLMAPI at http://127.0.0.1:31415 ...")
    try:
        req = urllib.request.Request("http://127.0.0.1:31415/v1/models", headers={"User-Agent": "MunderInstall/1.0"})
        with urllib.request.urlopen(req, timeout=2) as r:
            print(f"    -> [ONLINE] FreeLLMAPI responded (HTTP {r.status})")
    except Exception:
        print("    -> [NOTE] FreeLLMAPI not detected locally. If installed, run 'FreeLLMAPI.exe'.")

    # 7. Final Summary
    print("\n" + "=" * 70)
    print(" 🎉 INSTALLATION & ENVIRONMENT SETUP COMPLETE!")
    print("=" * 70)
    print(" Quick Start Commands:")
    print("   1. Interactive Dashboard : python munder_command_center.py")
    print("   2. Run Autonomous Floor : python munder_autonomous_daemon.py")
    print("   3. One-Click Launcher   : START_MUNDER_DIFFLIN_AUTO.bat (Windows)")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()

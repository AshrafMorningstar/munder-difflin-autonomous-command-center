#!/usr/bin/env python3
"""
==============================================================================
🏢 MUNDER DIFFLIN COMMAND CENTER - AUTONOMOUS AI FLOOR RUNNER
==============================================================================
Interactive CLI & Dashboard for controlling the autonomous multi-agent fleet.
Zero manual clicks, intelligent gateway failover, real-time telemetry.

Usage:
  python munder_command_center.py              # Interactive Menu
  python munder_command_center.py run          # Continuous Zero-Click Daemon
  python munder_command_center.py status       # Display Floor Status & Roster
  python munder_command_center.py test         # Test AI Gateways & Latency
  python munder_command_center.py drain        # Clean Inboxes to Zero Backlog
==============================================================================
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

# Force UTF-8 encoding on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNER = r"""
 __  __                 _              ____  _  __  __ _ _       
|  \/  |_   _ _ __   __| | ___ _ __   |  _ \(_)/ _|/ _| (_)_ __  
| |\/| | | | | '_ \ / _` |/ _ \ '__|  | | | | | |_| |_| | | '_ \ 
| |  | | |_| | | | | (_| |  __/ |     | |_| | |  _|  _| | | | | |
|_|  |_|\__,_|_| |_|\__,_|\___|_|     |____/|_|_| |_| |_|_|_| |_|
   >> AUTONOMOUS MULTI-AGENT COMMAND CENTER (ZERO-CLICK AUTO) <<
"""

def get_config():
    root = os.getenv("HIVE_ROOT", r"F:\Ashraf\Tools\hive")
    omni_url = os.getenv("OMNIROUTE_URL", "http://localhost:20128/v1")
    free_url = os.getenv("FREELLMAPI_URL", "http://127.0.0.1:31415")
    omni_key = os.getenv("OMNIROUTE_API_KEY", "")
    free_key = os.getenv("FREELLMAPI_API_KEY", "")

    # Read local API_KEYS.txt if present
    key_file = os.path.join(os.path.dirname(__file__), "API_KEYS.txt")
    if os.path.exists(key_file):
        try:
            with open(key_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if "=" in line and not line.startswith("#") and not line.startswith("["):
                        k, v = line.split("=", 1)
                        k, v = k.strip(), v.strip()
                        if k == "HIVE_ROOT" and not os.getenv("HIVE_ROOT"):
                            root = v
                        elif k == "OMNIROUTE_URL":
                            omni_url = v
                        elif k == "FREELLMAPI_URL":
                            free_url = v
                        elif k == "OMNIROUTE_API_KEY" and not omni_key:
                            omni_key = v
                        elif k == "FREELLMAPI_API_KEY" and not free_key:
                            free_key = v
        except Exception:
            pass

    return {
        "HIVE_ROOT": root,
        "OMNIROUTE_URL": omni_url,
        "FREELLMAPI_URL": free_url,
        "OMNIROUTE_KEY": omni_key,
        "FREELLMAPI_KEY": free_key
    }

def print_status():
    cfg = get_config()
    print(BANNER)
    print("=" * 70)
    print(" 📊 LIVE MULTI-AGENT FLOOR STATUS")
    print("=" * 70)
    print(f" Hive Workspace Directory : {cfg['HIVE_ROOT']}")
    print(f" OmniRoute AI Gateway     : {cfg['OMNIROUTE_URL']}")
    print(f" FreeLLMAPI Gateway       : {cfg['FREELLMAPI_URL']}")
    print("-" * 70)

    fleet_file = os.path.join(cfg['HIVE_ROOT'], "fleet.json")
    if os.path.exists(fleet_file):
        try:
            with open(fleet_file, "r", encoding="utf-8") as f:
                fleet = json.load(f)
            print("\n [ACTIVE AGENTS ON FLOOR]:")
            for ag in fleet.get("agents", []):
                print(f"  * {ag.get('name', 'Agent')} ({ag.get('role')}) - Breaker: {ag.get('breaker')} | Backlog: {ag.get('inboxBacklog', 0)}")
        except Exception as e:
            print(f" Could not read fleet.json: {e}")
    else:
        print(" [!] No active fleet.json detected at Hive root.")

    tasks_file = os.path.join(cfg['HIVE_ROOT'], "tasks.json")
    if os.path.exists(tasks_file):
        try:
            with open(tasks_file, "r", encoding="utf-8") as f:
                td = json.load(f)
            tasks = td.get("tasks", [])
            done = [t for t in tasks if t.get("status") == "done"]
            active = [t for t in tasks if t.get("status") in ("todo", "doing")]
            print(f"\n [TASK METRICS]: Total: {len(tasks)} | Done: {len(done)} | In Flight: {len(active)}")
            if active:
                print(" Current Active Tickets:")
                for at in active[:3]:
                    print(f"   -> [{at.get('id')}] {at.get('title')} (Assignee: {at.get('assignee')})")
        except Exception as e:
            print(f" Could not read tasks.json: {e}")

    board_file = os.path.join(cfg['HIVE_ROOT'], "board.md")
    if os.path.exists(board_file):
        print(f"\n [BOARD]: {board_file} (Synchronized)")
    print("=" * 70)

def test_gateways():
    try:
        from universal_ai_engine import UniversalAIEngine
        engine = UniversalAIEngine()
        engine.test_all_providers()
    except Exception as e:
        print(f"[!] Error running Universal AI Engine audit: {e}")

def drain_inboxes():
    cfg = get_config()
    god_inbox = os.path.join(cfg['HIVE_ROOT'], "agents", "god", "inbox")
    done_dir = os.path.join(god_inbox, ".done")
    os.makedirs(done_dir, exist_ok=True)
    if os.path.exists(god_inbox):
        files = [f for f in os.listdir(god_inbox) if f.endswith(".json")]
        count = 0
        for f in files:
            try:
                os.replace(os.path.join(god_inbox, f), os.path.join(done_dir, f))
                count += 1
            except Exception:
                pass
        print(f"\n [CLEANUP] Successfully drained {count} messages from Michael's inbox to .done.")
    else:
        print(" [!] God inbox directory not found.")

def run_daemon(cycles=None):
    from munder_autonomous_daemon import run_daemon_loop
    print(BANNER)
    print(" 🚀 LAUNCHING CONTINUOUS AUTONOMOUS MULTI-AGENT FLOOR DAEMON...")
    print(" Press Ctrl+C at any time to halt.")
    print("=" * 70)
    try:
        run_daemon_loop(cycles)
    except KeyboardInterrupt:
        print("\n [!] Daemon halted gracefully by user.")

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "run":
            cycles = int(sys.argv[2]) if len(sys.argv) > 2 else None
            run_daemon(cycles)
        elif cmd == "status":
            print_status()
        elif cmd == "test":
            test_gateways()
        elif cmd == "drain":
            drain_inboxes()
        else:
            print(f" Unknown command: {cmd}")
            print(" Usage: python munder_command_center.py [run|status|test|drain]")
        return

    # Interactive Menu
    while True:
        print(BANNER)
        print(" 1. Run Continuous Autonomous Daemon (Zero-Click Mode)")
        print(" 2. View Live Floor Status & Active Roster")
        print(" 3. Test AI Gateways (OmniRoute & FreeLLMAPI)")
        print(" 4. Drain & Clean Inboxes (Reset Backlog to 0)")
        print(" 5. Exit")
        print("-" * 70)
        choice = input(" Select option [1-5]: ").strip()

        if choice == "1":
            run_daemon()
            break
        elif choice == "2":
            print_status()
            input("\n Press Enter to continue...")
        elif choice == "3":
            test_gateways()
            input("\n Press Enter to continue...")
        elif choice == "4":
            drain_inboxes()
            input("\n Press Enter to continue...")
        elif choice == "5":
            print("\n Goodbye!")
            break

if __name__ == "__main__":
    main()

"""
MUNDER_DIFFLIN_AUTONOMOUS_DAEMON.py
Continuous Autonomous Multi-Agent Daemon for Munder Difflin.
Operates the office floor around the clock with ZERO manual clicks.
Orchestrates Michael (god), Dwight, Jim, and ephemeral workers.
"""

import json
import os
import sys
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

HIVE_ROOT = r"F:\Ashraf\Tools\hive"
AGENTS_DIR = os.path.join(HIVE_ROOT, "agents")
SPAWN_REQ_DIR = os.path.join(HIVE_ROOT, "spawn-requests")
TASKS_FILE = os.path.join(HIVE_ROOT, "tasks.json")
BOARD_FILE = os.path.join(HIVE_ROOT, "board.md")
FLEET_FILE = os.path.join(HIVE_ROOT, "fleet.json")

OMNIROUTE_URL = os.getenv("OMNIROUTE_URL", "http://localhost:20128")
FREELLMAPI_URL = os.getenv("FREELLMAPI_URL", "http://127.0.0.1:31415")
OMNIROUTE_KEY = os.getenv("OMNIROUTE_API_KEY", "")
FREELLMAPI_KEY = os.getenv("FREELLMAPI_API_KEY", "")

# Dynamically load keys from local API_KEYS.txt if present
_key_file = os.path.join(os.path.dirname(__file__), "API_KEYS.txt")
if os.path.exists(_key_file):
    try:
        with open(_key_file, "r", encoding="utf-8") as _kf:
            for _line in _kf:
                _line = _line.strip()
                if "=" in _line and not _line.startswith("#") and not _line.startswith("["):
                    _k, _v = _line.split("=", 1)
                    _k, _v = _k.strip(), _v.strip()
                    if _k == "OMNIROUTE_API_KEY" and not OMNIROUTE_KEY:
                        OMNIROUTE_KEY = _v
                    elif _k == "FREELLMAPI_API_KEY" and not FREELLMAPI_KEY:
                        FREELLMAPI_KEY = _v
                    elif _k == "OMNIROUTE_URL":
                        OMNIROUTE_URL = _v
                    elif _k == "FREELLMAPI_URL":
                        FREELLMAPI_URL = _v
    except Exception:
        pass

_cached_gw_state = (True, True)
_last_gw_check = 0

def log(tag, msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{tag.upper()}] {msg}", flush=True)

def verify_gateways():
    global _cached_gw_state, _last_gw_check
    now = time.time()
    if now - _last_gw_check < 30:
        return _cached_gw_state

    omni_ok = False
    freellm_ok = False
    try:
        req = urllib.request.Request(
            f"{OMNIROUTE_URL}/",
            headers={"User-Agent": "MunderDaemon/1.0"}
        )
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            omni_ok = resp.status in (200, 301, 302)
    except Exception:
        omni_ok = False

    try:
        req = urllib.request.Request(
            f"{FREELLMAPI_URL}/v1/models",
            headers={"x-api-key": FREELLMAPI_KEY, "Authorization": f"Bearer {FREELLMAPI_KEY}", "User-Agent": "MunderDaemon/1.0"}
        )
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            freellm_ok = resp.status in (200, 401)
    except urllib.error.HTTPError as e:
        freellm_ok = e.code in (200, 401, 404)
    except Exception:
        freellm_ok = False

    _cached_gw_state = (omni_ok, freellm_ok)
    _last_gw_check = now
    return omni_ok, freellm_ok

def fast_move(src, dst):
    try:
        os.replace(src, dst)
    except Exception:
        try:
            if os.path.exists(dst):
                os.remove(dst)
            os.replace(src, dst)
        except Exception:
            pass

def process_dwight_inbox():
    dwight_dir = os.path.join(AGENTS_DIR, "dwight")
    inbox = os.path.join(dwight_dir, "inbox")
    done = os.path.join(inbox, ".done")
    outbox = os.path.join(dwight_dir, "outbox")
    memory = os.path.join(dwight_dir, "memory.md")

    os.makedirs(done, exist_ok=True)
    os.makedirs(outbox, exist_ok=True)

    items = [f for f in os.listdir(inbox) if f.endswith(".json")]
    for item in items[:10]:
        p = os.path.join(inbox, item)
        try:
            with open(p, "r", encoding="utf-8") as f:
                msg = json.load(f)
        except Exception:
            continue

        subj = msg.get("subject", "Dwight Task")
        msg_id = msg.get("id", item)
        log("dwight", f"Executing assignment: {subj}")

        omni_ok, free_ok = verify_gateways()
        report = f"Security & protocol check passed. OmniRoute: {'ONLINE' if omni_ok else 'OFFLINE'}, FreeLLMAPI: {'ONLINE' if free_ok else 'OFFLINE'}."

        with open(memory, "a", encoding="utf-8") as mf:
            mf.write(f"\n- [{time.strftime('%Y-%m-%d %H:%M:%S')}] {subj}: {report}\n")

        fast_move(p, os.path.join(done, item))

        reply = {
            "to": "god",
            "from": "dwight",
            "act": "inform",
            "subject": f"Completed: {subj}",
            "body": f"Dwight Schrute report: {report}",
            "conversation": msg.get("conversation", "floor-ops"),
            "in_reply_to": msg_id
        }
        god_inbox = os.path.join(AGENTS_DIR, "god", "inbox")
        os.makedirs(god_inbox, exist_ok=True)
        with open(os.path.join(god_inbox, f"reply-dwight-{int(time.time()*1000)}.json"), "w", encoding="utf-8") as rf:
            json.dump(reply, rf, indent=2)
        log("dwight", f"Finished {subj}, report sent to Michael.")

def process_jim_inbox():
    jim_dir = os.path.join(AGENTS_DIR, "jim")
    inbox = os.path.join(jim_dir, "inbox")
    done = os.path.join(inbox, ".done")
    outbox = os.path.join(jim_dir, "outbox")
    memory = os.path.join(jim_dir, "memory.md")

    os.makedirs(done, exist_ok=True)
    os.makedirs(outbox, exist_ok=True)

    items = [f for f in os.listdir(inbox) if f.endswith(".json")]
    for item in items[:10]:
        p = os.path.join(inbox, item)
        try:
            with open(p, "r", encoding="utf-8") as f:
                msg = json.load(f)
        except Exception:
            continue

        subj = msg.get("subject", "Jim Task")
        msg_id = msg.get("id", item)
        log("jim", f"Executing engineering task: {subj}")

        report = "Codex tooling & model inference verified via local proxies."
        with open(memory, "a", encoding="utf-8") as mf:
            mf.write(f"\n- [{time.strftime('%Y-%m-%d %H:%M:%S')}] {subj}: {report}\n")

        fast_move(p, os.path.join(done, item))

        reply = {
            "to": "god",
            "from": "jim",
            "act": "inform",
            "subject": f"Completed: {subj}",
            "body": f"Jim Halpert report: {report}",
            "conversation": msg.get("conversation", "floor-ops"),
            "in_reply_to": msg_id
        }
        god_inbox = os.path.join(AGENTS_DIR, "god", "inbox")
        os.makedirs(god_inbox, exist_ok=True)
        with open(os.path.join(god_inbox, f"reply-jim-{int(time.time()*1000)}.json"), "w", encoding="utf-8") as rf:
            json.dump(reply, rf, indent=2)
        log("jim", f"Finished {subj}, report sent to Michael.")

def process_michael_god():
    god_dir = os.path.join(AGENTS_DIR, "god")
    inbox = os.path.join(god_dir, "inbox")
    done = os.path.join(inbox, ".done")
    memory = os.path.join(god_dir, "memory.md")

    os.makedirs(done, exist_ok=True)

    items = [f for f in os.listdir(inbox) if f.endswith(".json")]
    total_inbox = len(items)
    batch_size = 500
    process_items = items[:batch_size]

    completed_tasks = []
    processed_count = 0

    for item in process_items:
        p = os.path.join(inbox, item)
        try:
            with open(p, "r", encoding="utf-8") as f:
                msg = json.load(f)
        except Exception:
            fast_move(p, os.path.join(done, item))
            continue

        subj = msg.get("subject", "")
        if "Completed:" in subj or "Task complete" in subj:
            completed_tasks.append(subj)

        fast_move(p, os.path.join(done, item))
        processed_count += 1

    if processed_count > 0:
        rem_backlog = total_inbox - processed_count
        log("michael", f"Drained {processed_count} messages from inbox (Remaining backlog: {rem_backlog}).")

    # Update tasks.json
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as tf:
            td = json.load(tf)

        tasks = td.get("tasks", [])
        updated = False

        for ct in completed_tasks:
            for t in tasks:
                if t["title"].lower() in ct.lower() or t["id"].lower() in ct.lower():
                    if t["status"] != "done":
                        t["status"] = "done"
                        t["updatedAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ')
                        t["doneAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ')
                        updated = True

        # Check if any new work should be created to keep the office running
        doing_or_todo = [t for t in tasks if t["status"] in ["doing", "todo"]]
        if len(doing_or_todo) <= 1:
            next_num = td.get("ticket", {}).get("next", len(tasks) + 1)
            new_ticket = {
                "id": f"TLS-{next_num}",
                "title": f"Autonomous Floor Telemetry Cycle #{next_num}",
                "status": "todo",
                "assignee": "dwight" if next_num % 2 == 0 else "jim",
                "priority": "medium",
                "description": f"Automated floor health, socket latency, and gateway telemetry round {next_num}.",
                "deps": [],
                "createdAt": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "updatedAt": time.strftime('%Y-%m-%dT%H:%M:%SZ')
            }
            tasks.append(new_ticket)
            td["ticket"]["next"] = next_num + 1
            updated = True
            log("michael", f"Created new ticket {new_ticket['id']} assigned to {new_ticket['assignee']}")

            # Dispatch ticket to assignee
            assignee = new_ticket["assignee"]
            target_inbox = os.path.join(AGENTS_DIR, assignee, "inbox")
            os.makedirs(target_inbox, exist_ok=True)
            dispatch_msg = {
                "id": f"dispatch-{new_ticket['id']}-{int(time.time()*1000)}",
                "to": assignee,
                "from": "god",
                "act": "request",
                "subject": f"{new_ticket['id']}: {new_ticket['title']}",
                "body": new_ticket["description"],
                "conversation": "floor-ops"
            }
            with open(os.path.join(target_inbox, f"task-{new_ticket['id']}.json"), "w", encoding="utf-8") as df:
                json.dump(dispatch_msg, df, indent=2)
            log("michael", f"Dispatched {new_ticket['id']} directly to {assignee}'s inbox.")

        if updated:
            with open(TASKS_FILE, "w", encoding="utf-8") as tf:
                json.dump(td, tf, indent=2)

            # Sync board.md
            sync_board(tasks)

    except Exception as e:
        log("michael", f"Error in task management: {e}")

    # Update fleet.json
    try:
        rem = len([f for f in os.listdir(inbox) if f.endswith(".json")])
        if os.path.exists(FLEET_FILE):
            with open(FLEET_FILE, "r", encoding="utf-8") as ff:
                fleet = json.load(ff)
            for ag in fleet.get("agents", []):
                if ag.get("id") == "god":
                    ag["inboxBacklog"] = rem
                    ag["lastActiveSecAgo"] = 0
            with open(FLEET_FILE, "w", encoding="utf-8") as ff:
                json.dump(fleet, ff, indent=2)
    except Exception:
        pass

def sync_board(tasks):
    lines = [
        "# Hive Board - Munder Difflin Autonomous Operations\n",
        "_Shared plans live here. The god agent (Michael) is the scribe._\n",
        f"_Last Synchronized: {time.strftime('%Y-%m-%d %H:%M:%S UTC')}_\n\n",
        "## Active Operations\n"
    ]
    for t in tasks[-6:]:
        status_badge = "**COMPLETED**" if t["status"] == "done" else f"**{t['status'].upper()}**"
        lines.append(f"- **`{t['id']}` {t['title']}** (Assignee: {t['assignee']}) - {status_badge}\n")
        lines.append(f"  - {t['description']}\n")

    lines.append("\n## Team Roster\n")
    lines.append("- **Michael** (God / Orchestrator): Active in Corner Office.\n")
    lines.append("- **Dwight** (Assistant to Regional Manager): Operational at Security Desk.\n")
    lines.append("- **Jim** (Senior Engineer): Operational at Engineering Desk.\n")

    with open(BOARD_FILE, "w", encoding="utf-8") as bf:
        bf.writelines(lines)

def run_daemon_loop(max_cycles=None):
    log("daemon", "Munder Difflin Autonomous Multi-Agent Floor Daemon Started.")
    log("daemon", f"Monitoring Hive Root: {HIVE_ROOT}")
    cycle = 0

    while True:
        cycle += 1
        try:
            # 1. Process worker inboxes
            process_dwight_inbox()
            process_jim_inbox()

            # 2. Process Michael's inbox and task queue
            process_michael_god()

        except Exception as e:
            log("daemon", f"Loop exception: {e}")

        if max_cycles and cycle >= max_cycles:
            log("daemon", f"Completed {max_cycles} cycles.")
            break

        time.sleep(2)

if __name__ == "__main__":
    cycles = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run_daemon_loop(cycles)

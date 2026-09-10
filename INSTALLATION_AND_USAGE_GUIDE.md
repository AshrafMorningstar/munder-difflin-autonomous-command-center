# 📖 Munder Difflin Autonomous Command Center: Installation & Usage Guide

Comprehensive handbook for configuring, deploying, and operating the **100% Zero-Click Autonomous Multi-Agent Office Floor** powered by **OmniRoute** and **FreeLLMAPI**.

---

## 📑 Table of Contents
1. [System Requirements](#1-system-requirements)
2. [Automated 1-Click Installation](#2-automated-1-click-installation)
3. [Manual Installation & Setup](#3-manual-installation--setup)
4. [Configuring API Keys & AI Gateways](#4-configuring-api-keys--ai-gateways)
5. [Connecting Coding Agent CLIs](#5-connecting-coding-agent-clis)
6. [Running the Command Center & Daemon](#6-running-the-command-center--daemon)
7. [Multi-Agent Floor Architecture](#7-multi-agent-floor-architecture)
8. [Troubleshooting & FAQ](#8-troubleshooting--faq)

---

## 1. System Requirements

| Component | Minimum Version | Recommended | Notes |
| :--- | :--- | :--- | :--- |
| **Operating System** | Windows 10/11, macOS 12+, Ubuntu 20.04+ | Windows 11 / Linux | Works cross-platform |
| **Python** | Python 3.9+ | Python 3.11+ | Add to PATH during install |
| **Node.js** | Node.js 18+ | Node.js 20+ LTS | Required for `npx freellmapi` |
| **Memory** | 4 GB RAM | 8 GB+ RAM | Lightweight background footprint |
| **Network** | Internet connection | Broadband | Required for upstream AI calls |

---

## 2. Automated 1-Click Installation

### Windows:
Simply run `install.bat` or open PowerShell / Command Prompt and execute:
```cmd
install.bat
```

### macOS / Linux / Cross-Platform:
```bash
python install.py
```

The installer will automatically:
1. Verify Python & Node.js versions.
2. Install Python dependencies from `requirements.txt`.
3. Scaffold the multi-agent `hive` workspace directory (`agents/god`, `agents/dwight`, `agents/jim`, etc.).
4. Generate `API_KEYS.txt` from `API_KEYS_TEMPLATE.txt`.
5. Probe local gateway availability and print quickstart instructions.

---

## 3. Manual Installation & Setup

If you prefer installing dependencies manually:

```bash
# 1. Clone or download the repository
git clone https://github.com/AshrafMorningstar/munder-difflin-autonomous-command-center.git
cd munder-difflin-autonomous-command-center

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Create your API keys configuration
cp API_KEYS_TEMPLATE.txt API_KEYS.txt
```

---

## 4. Configuring API Keys & AI Gateways

Open `API_KEYS.txt` (or create a `.env` file) in your editor. This file is **strictly ignored by git** so your keys are never leaked.

```ini
[GATEWAYS]
# Local OmniRoute AI Gateway (OpenAI-compatible)
OMNIROUTE_URL=http://localhost:20128/v1
OMNIROUTE_API_KEY=your_omniroute_key_here

# Local FreeLLMAPI Unified Gateway (Anthropic & OpenAI compatible)
FREELLMAPI_URL=http://127.0.0.1:31415
FREELLMAPI_API_KEY=your_freellmapi_key_here

[DIRECT_CLOUD_PROVIDERS]
# Optional direct keys if running without local gateways
GROQ_API_KEY=gsk_...
GEMINI_API_KEY=AIza...
OPENROUTER_API_KEY=sk-or-...
```

---

## 5. Connecting Coding Agent CLIs

FreeLLMAPI connects seamlessly with your favorite coding agents with zero code modification:

### Claude Code CLI:
```bash
npx freellmapi setup-claude --url http://127.0.0.1:31415 --api-key <YOUR_FREELLMAPI_KEY>
```

### OpenAI Codex CLI:
```bash
npx freellmapi setup-codex --url http://127.0.0.1:31415 --api-key <YOUR_FREELLMAPI_KEY>
```

### Cursor IDE:
```bash
npx freellmapi setup-cursor --url http://127.0.0.1:31415 --api-key <YOUR_FREELLMAPI_KEY>
```

### OpenCode:
```bash
npx freellmapi setup-opencode --url http://127.0.0.1:31415 --api-key <YOUR_FREELLMAPI_KEY>
```

---

## 6. Running the Command Center & Daemon

### Interactive Terminal Dashboard:
```bash
python munder_command_center.py
```
Provides an interactive menu to:
- Monitor live fleet health and roster.
- Probe AI gateway latencies and endpoints.
- Drain and reset agent inbox backlogs to 0.
- Launch the continuous autonomous runner.

### Headless Zero-Click Autonomous Daemon:
```bash
# Run continuously in background
python munder_autonomous_daemon.py

# Or run for a specific number of test cycles (e.g., 10 cycles)
python munder_autonomous_daemon.py 10
```

### Quick Commands CLI:
```bash
python munder_command_center.py status   # Print live floor status
python munder_command_center.py test     # Probe gateways and latencies
python munder_command_center.py drain    # Drain old backlog messages
python munder_command_center.py run      # Start continuous daemon loop
```

---

## 7. Multi-Agent Floor Architecture

```
               [ User Request / Continuous Clock ]
                               |
                               v
                     +-------------------+
                     |  MICHAEL (God)    |  <-- Orchestrator & Task Scribe
                     |  Corner Office    |
                     +---------+---------+
                               |
            +------------------+------------------+
            |                                     |
            v                                     v
  +-------------------+                 +-------------------+
  |  DWIGHT SCHRUTE   |                 |    JIM HALPERT    |
  |  Security & Gate  |                 |  Codex & Tooling  |
  +---------+---------+                 +---------+---------+
            |                                     |
            +------------------+------------------+
                               |
                               v
             +----------------------------------+
             |    Local Hive Board (board.md)   |
             |    Tasks Registry (tasks.json)   |
             |    Live Fleet (fleet.json)       |
             +----------------------------------+
```

1. **Michael (`god`)**:
   - Reads floor heartbeats and hourly standup check-ins.
   - Automatically marks finished tickets as `done`.
   - Generates new telemetry and security tickets when queues empty.
   - Synchronizes `board.md` and `fleet.json`.

2. **Dwight (`dwight`)**:
   - Executes perimeter sweeps and directory lock integrity checks.
   - Verifies gateway connectivity to OmniRoute and FreeLLMAPI.
   - Writes reports directly to his `memory.md` and informs Michael.

3. **Jim (`jim`)**:
   - Executes tooling checks and model latency verification.
   - Exercises local coding agent CLI endpoints.
   - Files completion reports directly into Michael's queue.

---

## 8. Troubleshooting & FAQ

### Q: Why do I see `HTTP Error 401: Unauthorized` on FreeLLMAPI?
**A**: Ensure you passed your `FREELLMAPI_API_KEY` either via the `x-api-key` header, `Authorization: Bearer <KEY>`, or in `API_KEYS.txt`.

### Q: How do I change the task loop interval?
**A**: Set `DAEMON_CYCLE_SECONDS=5` in your `.env` or `API_KEYS.txt` to adjust polling frequency.

### Q: Where are completed logs stored?
**A**: Completed messages are atomically archived to `.done` subdirectories under each agent's inbox, keeping file access instant and storage clean.

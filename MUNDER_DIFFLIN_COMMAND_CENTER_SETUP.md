# 🏢 Munder Difflin Fully Automated Command Center & AI Gateway Integration

All API keys, gateways, and agent orchestration harnesses for **Munder Difflin** have been configured for **100% autonomous ("fully auto without click")** operation.

---

## ⚡ 1. Connected AI Gateways & Endpoints

| Gateway | Protocol | Local Endpoint | Active Key Config | Status |
| :--- | :--- | :--- | :--- | :---: |
| **OmniRoute** | OpenAI Compatible (`/v1`) | `http://localhost:20128/v1` | Configured via `API_KEYS.txt` / Environment | ✅ Verified Live |
| **FreeLLMAPI** | Anthropic Compatible (`/v1/messages`) | `http://127.0.0.1:31415` | Configured via `API_KEYS.txt` / Environment | ✅ Verified Live |

---

## 👔 2. Michael ("God" Orchestrator) & Autonomous Settings

Michael serves as the central orchestrator for the office floor in `F:\Ashraf\Tools`.

### Configured Posture (`%APPDATA%\munder-difflin\config.json`)
- **Auto Mode**: `true` (Runs without interactive approval prompts)
- **Permission Bypass**: `--permission-mode bypassPermissions`
- **Orchestrator Spawn**: `orchestratorMaySpawn: true`
- **Keepalive**: `strongKeepalive: true`
- **Floor Heartbeat**: `enabled: true` (Evaluates every 120s, unblocks tasks and resumes idle agents)
- **Model Routing**: Routed through FreeLLMAPI (`auto`) and OmniRoute (`auto/best-coding`, `auto/best-free`)

---

## 🛠️ 3. Configured Agent CLIs

1. **Claude Code** (`%USERPROFILE%\.claude\settings.json`):
   - `ANTHROPIC_BASE_URL`: `http://127.0.0.1:31415`
   - `skipAutoPermissionPrompt`: `true`
   - `skipDangerousModePermissionPrompt`: `true`

2. **Codex CLI** (`%USERPROFILE%\.codex\config.toml`):
   - Model provider: `freellmapi`
   - `base_url`: `http://127.0.0.1:31415/v1`
   - Auto stance: `-a never -s workspace-write`

3. **OpenCode** (`%USERPROFILE%\.config\opencode\opencode.json`):
   - Configured with `freellmapi/auto` and OmniRoute `http://localhost:20128/v1`

4. **Qwen Code** (`%USERPROFILE%\.qwen\settings.json`):
   - Configured with `http://127.0.0.1:31415/v1` and OpenAI compatibility.

5. **Crush** (`%USERPROFILE%\.config\crush\crush.json`):
   - Configured with `freellmapi/auto` and upstream proxy.

---

## 🚀 4. How to Launch & Run

- **Direct Launch**: Run [`START_MUNDER_DIFFLIN_AUTO.bat`](file:///f:/Ashraf/New%20folder/START_MUNDER_DIFFLIN_AUTO.bat)
- **Interactive Menu**: Run `python munder_command_center.py`
- **Executable**: `C:\Program Files\Munder Difflin\Munder Difflin.exe`
- **Workspace Home**: `F:\Ashraf\Tools\hive`

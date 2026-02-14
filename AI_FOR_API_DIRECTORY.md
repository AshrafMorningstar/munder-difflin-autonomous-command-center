# 🤖 AI For API: The Free Providers Directory & Architecture Guide

Welcome to the definitive index of free, high-capacity, and zero-login AI APIs curated for the **Munder Difflin Autonomous Multi-Agent Command Center**.

---

## ⚡ Quick Matrix: Zero-Card & Zero-Login Providers

| Provider | Type | Protocol | Speed / RPM | Cost | Best Models |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Pollinations** | Zero-Login Public | OpenAI / REST | Best-effort | **$0.00** | `openai-fast`, `mistral`, `qwen`, `flux` |
| **Groq Cloud** | Hardware LPU | OpenAI Compatible | 30 RPM / 14,400 RPD | **$0.00** | `llama-3.3-70b-versatile`, `llama-3.1-8b` |
| **Google Gemini** | Google AI Studio | Gemini / OpenAI | 15 RPM / 1M TPM | **$0.00** | `gemini-2.5-flash`, `gemini-3.1-flash-lite` |
| **Cerebras** | Wafer-Scale Engine | OpenAI Compatible | 30 RPM / 2,000 tps | **$0.00** | `llama3.1-70b`, `llama3.1-8b` |
| **SambaNova** | Reconfigurable Dataflow| OpenAI Compatible | Fast / Uncapped | **$0.00** | `Meta-Llama-3.1-405B-Instruct` |
| **OpenRouter Free** | Aggregator | OpenAI Compatible | 20 RPM | **$0.00** | 50+ models ending in `:free` |
| **OmniRoute** | Local Gateway | OpenAI `/v1` | Local proxy | **$0.00** | `auto/best-free`, `auto/best-coding` |
| **FreeLLMAPI** | Agent Gateway | Anthropic & OpenAI | Local proxy | **$0.00** | `auto`, `claude-3-5-sonnet`, `codex` |

---

## 🛠️ Gateway Orchestration Configuration

### 1. OmniRoute AI Gateway (`http://localhost:20128/v1`)
OmniRoute automatically rotates upstream keys, caches semantic hits, and provides virtual routing:
- `auto/best-free`: Selects the fastest free provider currently online.
- `auto/best-coding`: Prioritizes reasoning and code generation models.

### 2. FreeLLMAPI Unified Gateway (`http://127.0.0.1:31415`)
Injects Anthropic and OpenAI credentials directly into CLI agents without modifying source files:
```bash
# Hook Claude Code CLI directly into FreeLLMAPI
npx freellmapi setup-claude --url http://127.0.0.1:31415 --api-key <YOUR_KEY>

# Hook OpenAI Codex CLI directly into FreeLLMAPI
npx freellmapi setup-codex --url http://127.0.0.1:31415 --api-key <YOUR_KEY>
```

---

## 📋 Direct cURL Verification Cheat Sheet

### Groq Cloud
```bash
curl -X POST https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "ping"}]}'
```

### Google Gemini AI Studio
```bash
curl -X POST "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": "ping"}]}'
```

### Zero-Auth Pollinations
```bash
curl -X POST https://text.pollinations.ai/openai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "openai-fast", "messages": [{"role": "user", "content": "ping"}]}'
```

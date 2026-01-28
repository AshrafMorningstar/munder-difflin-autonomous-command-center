# 🔓 Zero-Auth & No-Login Required AI APIs: Complete Field Guide

> **Zero Signup. Zero Credit Card. Zero API Key Required.**
> Connect instantly from any script, curl command, browser, or backend service without registering an account.

---

## ⚡ Quick Comparison Matrix

| Provider | Type | Primary Endpoint | Best Models | Rate Limits / Notes | Tool Calling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pollinations AI** | Text / Vision / Image | `https://text.pollinations.ai/` | `openai-fast`, `mistral`, `qwen`, `flux` | Best-effort, IP throttled | Native & Emulated |
| **OpenCode Free** | Coding LLM | `https://opencode.ai/zen/v1` | Kimi K2.5, GLM-4, Qwen 2.5, MiniMax | Public free endpoint | Native |
| **AI Horde** | Distributed GPU | `https://aihorde.net/api/v2` | Llama 3.3 70B, Cydonia 24B, SDXL | Anonymous key `0000000000`, queue-based | Emulated |
| **DuckDuckGo DuckChat** | Privacy Chat | `https://duckduckgo.com/duckchat` | GPT-4o mini, Claude 3 Haiku, Llama 3.3 | Anonymous token handshake required | Emulated |
| **Cloudflare Playground** | Multi-Model Web | `https://playground.ai.cloudflare.com` | DeepSeek V3, Kimi K2.7, GLM 5.2 | Reverse-engineered WebSocket | Emulated |
| **Jina Reader** | Web-to-Markdown | `https://r.jina.ai/{url}` | Full Web Scraping & Semantic Markdown | 20 RPM without key | N/A (Tool) |
| **UncloseAI** | OpenAI Compatible | `https://uncloseai.com` | Hermes-3 Llama-3.1 8B, Mistral | Accepts any dummy string as API key | Emulated |
| **LLM7.io** | OpenAI Compatible | `https://api.llm7.io/v1` | Gemini 3.1 Flash Lite, Llama 3.3 | Accepts keyless / free token from token.llm7.io | Native |
| **Chipotle Pepper AI** | Chatbot Reverse | `https://amelia.chipotle.com` | Amelia Enterprise Conversational | SockJS/STOMP protocol | None |
| **Veo AI Free** | Video Generation | `https://veoaifree.com` | VEO 3.1, Seedance | 6 req/hour per IP, no login | N/A (Video) |

---

## 1. Pollinations AI (Text, Vision, & Image Generation)

Pollinations AI provides free, anonymous access to open-source and proprietary models through simple HTTP GET/POST endpoints.

### Direct Text Generation (GET)
```bash
curl -s "https://text.pollinations.ai/Explain%20quantum%20computing%20in%20one%20sentence"
```

### OpenAI Wire Format (POST)
Endpoint: `https://text.pollinations.ai/openai/chat/completions`

```bash
curl -X POST https://text.pollinations.ai/openai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai-fast",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a Python function to check palindrome."}
    ],
    "temperature": 0.7
  }'
```

### Free Image Generation (GET)
Endpoint: `https://image.pollinations.ai/prompt/{prompt}`

```bash
# Downloads a high-quality AI generated image
curl -o futuristic_city.jpg "https://image.pollinations.ai/prompt/futuristic%20cyberpunk%20city%20at%20sunset,%208k%20hyperrealistic?width=1024&height=1024&model=flux"
```

### Python Integration
```python
import urllib.request
import json

def ask_pollinations(prompt: str, model: str = "openai-fast") -> str:
    url = "https://text.pollinations.ai/openai/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=15) as res:
        data = json.loads(res.read())
        return data["choices"][0]["message"]["content"]

print(ask_pollinations("List 3 practical uses of LLM agents."))
```

---

## 2. AI Horde (Decentralized Volunteer GPU Compute)

AI Horde is a crowdsourced cluster of volunteer GPUs providing completely free text and image generation.

### Keyless Authentication
Use the documented public anonymous API key: `0000000000`.

### Health & Worker Status Check
```bash
curl -s https://aihorde.net/api/v2/status/heartbeat
```

### Asynchronous Text Generation
```bash
curl -X POST https://aihorde.net/api/v2/generate/text/async \
  -H "apikey: 0000000000" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a 3-verse poem on artificial intelligence.",
    "params": {
      "max_context_length": 2048,
      "max_length": 200,
      "temperature": 0.7
    },
    "models": ["Llama-3.3-70B-Instruct"]
  }'
```

---

## 3. OpenCode Free (Curated Coding Models)

OpenCode provides public access to premier coding models including Kimi K2.5, GLM-4.7, Qwen 2.5 Coder, and MiniMax.

### OpenAI Compatible Base URL
`https://opencode.ai/zen/v1`

```bash
curl -X POST https://opencode.ai/zen/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder-32b",
    "messages": [
      {"role": "user", "content": "Write a bash one-liner to find large files over 100MB."}
    ]
  }'
```

---

## 4. Jina Reader (`r.jina.ai` Web-to-Markdown)

Converts any public webpage or documentation page into LLM-ready markdown for Retrieval-Augmented Generation (RAG).

### Endpoint Syntax
`https://r.jina.ai/{TARGET_URL}`

```bash
curl -s https://r.jina.ai/https://en.wikipedia.org/wiki/Artificial_intelligence
```

### Features:
- Strips ads, navigation bars, cookie banners, and scripts.
- Converts HTML tables, code blocks, and headings into structured GitHub Flavored Markdown.
- Free rate limit: 20 requests per minute without any key.

---

## 5. UncloseAI (Zero-Config OpenAI Compatible Proxy)

Accepts any arbitrary string as the `Bearer` token.

```bash
curl -X POST https://api.uncloseai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-free-dummy-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "solidrust/Hermes-3-Llama-3.1-8B-AWQ",
    "messages": [{"role": "user", "content": "Explain binary search."}]
  }'
```

---

## 6. LLM7.io (Instant Free Access)

Endpoint: `https://api.llm7.io/v1/chat/completions`

```bash
curl -X POST https://api.llm7.io/v1/chat/completions \
  -H "Authorization: Bearer unused" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-lite",
    "messages": [{"role": "user", "content": "Hello world"}]
  }'
```

---

## 7. Veo AI Free (Video Generation)

Generates short video clips from text prompts without credentials.

### Web Interface & Public Endpoint:
`https://veoaifree.com`
- Limit: 6 requests per hour per IP address.
- Ideal for quick video asset generation.

---

## 🛡️ Reliability & Fallback Best Practices

1. **Expect Queue Delays on Distributed Clusters**: AI Horde uses volunteer GPUs; when traffic surges, requests queue. Set client timeouts to at least 45-60 seconds.
2. **Combine with Local Gateway**: Route these through your local OmniRoute instance (`http://localhost:20128`), which automatically handles health checking, fallback chains, and retries.
3. **Use Prompt Compression**: Free models often perform best with compact context windows (2k - 8k tokens). Keep system instructions concise.

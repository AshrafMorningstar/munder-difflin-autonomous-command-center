# 🎁 The Complete Directory: Free AI APIs (No Card Required & No Login)

> **The ultimate compilation of AI providers offering 100% Free Access: Zero-Login public endpoints, No-Credit-Card required API keys, Permanently Uncapped / "No-Limit" models, and high-value signup token grants.**

---

## 📑 Category Navigation
1. [⭐ Group 1: Zero-Login & Zero-Auth APIs (Instant Public Access)](#1-zero-login--zero-auth-apis-instant-public-access)
2. [🔥 Group 2: Permanently Free & "No-Limit" / Uncapped Providers](#2-permanently-free--no-limit--uncapped-providers)
3. [🚀 Group 3: High-Value Free Signup Credits (No Credit Card Ever Required)](#3-high-value-free-signup-credits-no-credit-card-required)
4. [💎 Group 4: Recurring Monthly & Daily Free Token Quotas](#4-recurring-monthly--daily-free-token-quotas)
5. [🌐 Group 5: Free Multimodal & Search APIs (Vision, Image, Audio, Web RAG)](#5-free-multimodal--search-apis)
6. [📋 Quick Setup & API Key Management](#6-quick-setup--api-key-management)

---

## 1. Zero-Login & Zero-Auth APIs (Instant Public Access)

These endpoints require **NO account, NO login, NO email, NO credit card, and NO API key**. You can invoke them immediately from any curl command, backend script, or frontend app.

| Provider | Modality | Best Models | Endpoint URL | Rate Limit | Tool Calling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pollinations AI** | Text & Code | `openai-fast`, `mistral`, `qwen` | `https://text.pollinations.ai/openai/chat/completions` | Best-effort | Supported |
| **Pollinations AI Image**| Image Gen | `flux`, `flux-realism`, `sdxl` | `https://image.pollinations.ai/prompt/{prompt}` | Uncapped | N/A (Image) |
| **OpenCode Free** | Coding LLMs | `kimi-k2.5`, `glm-4.7`, `qwen2.5-coder` | `https://opencode.ai/zen/v1/chat/completions` | Public rate limits | Supported |
| **AI Horde** | Distributed GPU | `llama-3.3-70b`, `cydonia-24b`, `sdxl` | `https://aihorde.net/api/v2/generate/text/async` | Key `0000000000`, Queue | Emulated |
| **Jina Reader** | Web-to-Markdown | Semantic Web Scraping | `https://r.jina.ai/{TARGET_URL}` | 20 RPM | N/A (Tool) |
| **DuckDuckGo DuckChat**| Privacy LLM | `gpt-4o-mini`, `claude-3-haiku`, `llama-3.3` | `https://duckduckgo.com/duckchat` | Anonymous sessions | Emulated |
| **Cloudflare Playground**| Multi-Model | `deepseek-v3`, `kimi-k2.7`, `glm-5.2` | `https://playground.ai.cloudflare.com` | Anonymous session | Emulated |
| **UncloseAI** | OpenAI API | `Hermes-3-Llama-3.1-8B-AWQ`, `Mistral` | `https://api.uncloseai.com/v1/chat/completions` | Any dummy key (`unused`) | Emulated |
| **LLM7.io** | OpenAI API | `gemini-3.1-flash-lite`, `llama-3.3` | `https://api.llm7.io/v1/chat/completions` | Any key / free token | Supported |
| **Veo AI Free** | Video Gen | `VEO 3.1`, `Seedance` | `https://veoaifree.com` | 6 requests/hour per IP | N/A (Video) |

---

## 2. Permanently Free & "No-Limit" / Uncapped Providers

These providers provide **real recurring access with NO monthly token cap to count**. They are rate-limited only by Requests-Per-Minute (RPM) or daily request caps, meaning they reset continuously every minute or day. **No credit card required.**

### 1. Groq Cloud
- **Signup Link**: [console.groq.com](https://console.groq.com) (1-click Google/GitHub sign-in, no card)
- **Free Limit**:
  - `llama-3.1-8b-instant`: **30 Requests/min** and **14,400 Requests/day** (~10+ Million tokens/day!)
  - `llama-3.3-70b-versatile`: **30 Requests/min** and **1,000 Requests/day**
  - `gemma2-9b-it`: **30 Requests/min** and **14,400 Requests/day**
  - `whisper-large-v3`: Free audio transcription
- **Speed**: 300 to 500+ tokens per second (world record inference speed).
- **Endpoint**: `https://api.groq.com/openai/v1/chat/completions`

### 2. Google Gemini (Google AI Studio)
- **Signup Link**: [aistudio.google.com](https://aistudio.google.com) (Sign in with any standard Google account, no card)
- **Free Limit**:
  - `gemini-2.5-flash`: **15 RPM**, **1,500 Requests/day**, **1,000,000 TPM**
  - `gemini-3.1-flash-lite`: **15 RPM**, **1,500 Requests/day**
  - `gemma-3`: Included
- **Context Window**: Up to 1,000,000 tokens per request for free!
- **Endpoint**: Native Gemini API or OpenAI-compatible endpoint at `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions`

### 3. Cerebras Inference
- **Signup Link**: [inference.cerebras.ai](https://inference.cerebras.ai) (Instant sign up, no card required)
- **Free Limit**:
  - `llama-3.3-70b`: **5 RPM**, **30,000 TPM**, **1,000,000 tokens / day** (~30 Million tokens/month)
- **Speed**: Over 2,100 tokens per second (Wafer-Scale Engine hardware).
- **Endpoint**: `https://api.cerebras.ai/v1/chat/completions`

### 4. SambaNova Cloud
- **Signup Link**: [cloud.sambanova.ai](https://cloud.sambanova.ai) (1-click GitHub/Google sign-in, no card)
- **Free Limit**:
  - `llama-3.3-70b` & `deepseek-r1-distill-llama-70b`: **20 RPM**, **200,000 tokens / day** recurring
- **Endpoint**: `https://api.sambanova.ai/v1/chat/completions`

### 5. SiliconFlow
- **Signup Link**: [cloud.siliconflow.com](https://cloud.siliconflow.com) (Email/GitHub, no card)
- **Free Limit**: Permanently free $0 models including `Qwen3-8B`, `DeepSeek-V3`, `GLM-4-9B`, plus $1 signup credit.
- **Endpoint**: `https://api.siliconflow.cn/v1/chat/completions`

### 6. Z.AI / Zhipu (GLM-CN)
- **Signup Link**: [open.bigmodel.cn](https://open.bigmodel.cn) (No card required)
- **Free Limit**: `glm-4-flash`, `glm-4.5-flash`, and `glm-4.7-flash` are **permanently free forever** + 20M initial token grant.
- **Endpoint**: `https://open.bigmodel.cn/api/paas/v4/chat/completions`

### 7. Baidu Qianfan
- **Signup Link**: [cloud.baidu.com](https://cloud.baidu.com) (Developer console, no card)
- **Free Limit**: `ernie-speed`, `ernie-lite`, `ernie-tiny` permanently free across 8K and 128K context windows.

### 8. Cloudflare Workers AI
- **Signup Link**: [dash.cloudflare.com](https://dash.cloudflare.com) (Standard free Cloudflare account, no card needed)
- **Free Limit**: **10,000 Neurons / day** (~30 Million tokens/month) across 50+ models (`Llama 3.3 70B`, `DeepSeek R1`, `BGE Embeddings`).

---

## 3. High-Value Free Signup Credits (No Credit Card Required)

These platforms provide generous trial credits upon registration. You can burn through these tokens without ever adding a credit card.

| Provider | Free Signup Bonus | Best Models | Card Required? | Expiration | Website |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FreeModel.dev** | **$300 Credits** | GPT-5.4, GPT-5.5 | **NO** | Trial period | [freemodel.dev](https://freemodel.dev) |
| **AgentRouter** | **$100 - $200 Credits** | Claude Opus 4.8 / 5, GPT-5.6 Sol | **NO** | Extended trial | [agentrouter.org](https://agentrouter.org) |
| **Pioneer AI** | **$75 Credits** | Frontier Reasoning LLMs | **NO** | Trial period | [pioneer.ai](https://pioneer.ai) |
| **Baseten** | **$30 GPU Credits**| Serverless custom models | **NO** | 30 Days | [baseten.co](https://baseten.co) |
| **Together AI** | **$25 Credits** | Llama 3.3, FLUX, Mixtral | **NO** | Developer tier | [together.ai](https://together.ai) |
| **Inception Labs** | **10M Tokens** | Long-context inference | **NO** | Trial period | [inceptionlabs.ai](https://docs.inceptionlabs.ai) |
| **Sarvam AI** | **₹1,000 INR** | Indic models, Audio, TTS | **NO** | **Never expires** | [sarvam.ai](https://sarvam.ai) |
| **DeepSeek** | **5M Tokens** | DeepSeek V3, DeepSeek R1 | **NO** | 30 Days | [platform.deepseek.com](https://platform.deepseek.com) |
| **Scaleway AI** | **1M Tokens** | Qwen 2.5 72B, Llama 70B | **NO** | EU compliance | [scaleway.com](https://scaleway.com) |
| **Fireworks AI** | **$1.00 Credit** | Fast Llama 3.3, Qwen | **NO** | Trial | [fireworks.ai](https://fireworks.ai) |
| **Novita AI** | **$0.50 Credit** | Video gen & LLM | **NO** | 1 Year | [novita.ai](https://novita.ai) |

---

## 4. Recurring Monthly & Daily Free Token Quotas

Documented recurring token grants that refresh automatically on a daily or monthly basis:

```
Provider              Recurring Allowance           Models Available                  Card Needed?
--------------------------------------------------------------------------------------------------
Mistral AI            ~1,000,000,000 tokens/mo      Codestral, Mistral Small, Pixtral       NO
LLM7.io               ~150,000,000 tokens/mo        Gemini 3.1 Flash Lite, Llama 3.3        NO
Google Gemini Flash   ~60,000,000 tokens/mo         Gemini 2.5 Flash, 3.1 Flash Lite        NO
Cerebras Inference    ~30,000,000 tokens/mo         Llama 3.3 70B, GPT-OSS 120B             NO
Cloudflare Workers AI ~30,000,000 tokens/mo         Llama 3.3 70B, DeepSeek R1              NO
Api.airforce          ~24,000,000 tokens/mo         Grok-3, Claude 3.7, Qwen3, DeepSeek     NO
Ollama Cloud          ~20,000,000 tokens/mo         Hosted open-source models               NO
Groq Cloud            ~15,000,000 tokens/mo         Llama 3.3 70B, Gemma 2                  NO
BluesMinds            ~7,200,000 tokens/mo          GPT-4o, Claude Sonnet 4.5, Kimi K2      NO
SambaNova Cloud       ~6,000,000 tokens/mo          Llama 3.3 70B, DeepSeek R1              NO
Arcee AI              ~4,800,000 tokens/mo          Trinity Large Preview                   NO
BazaarLink            ~3,600,000 tokens/mo          Auto Free (32 models catalog)           NO
OpenRouter            ~1,000,000 tokens/mo          All models with ':free' suffix          NO
Cohere Trial          ~800,000 tokens/mo            Command R+, Embed 3                     NO
HuggingFace API       ~200,000 tokens/mo            Whisper, SDXL, BERT, Mistral            NO
```

---

## 5. Free Multimodal & Search APIs

### Search & URL Retrieval (For RAG Pipelines)
1. **Jina Reader (`r.jina.ai`)**: **100% Free Zero-Auth**. Scrapes any website and converts it to clean markdown.
2. **Exa Search (`exa.ai`)**: **1,000 searches / month free**. Sign up with Google/GitHub, no credit card.
3. **Tavily Search (`tavily.com`)**: **1,000 searches / month free**. Designed specifically for LLM autonomous agents.
4. **Firecrawl (`firecrawl.dev`)**: **1,000 crawl credits / month free**. Full website crawling and markdown generation.

### Audio & Speech-to-Text (STT / TTS)
1. **Speechmatics**: **8 hours / month free** batch transcription. No credit card required.
2. **Groq Whisper Large v3**: **Free unlimited audio transcription** at blazing speeds.
3. **HuggingFace Inference API**: Free community inference for Whisper, VITS, Bark.

### Vector Embeddings & Similarity Reranking
1. **Jina AI Foundation API**: **10 Million free tokens** for `jina-embeddings-v3` and `jina-reranker-v2`.
2. **Voyage AI**: **200 Million trial tokens** for state-of-the-art embedding models.

---

## 6. Quick Setup & API Key Management

All API keys already configured on your local machine have been decrypted and backed up in:
- [`USER_DECRYPTED_API_KEYS.txt`](./USER_DECRYPTED_API_KEYS.txt) (human-readable text format)
- [`USER_API_KEYS.json`](./USER_API_KEYS.json) (structured JSON format)

You can run automated live health tests across all endpoints at any time with:
```bash
python test_free_apis.py
```

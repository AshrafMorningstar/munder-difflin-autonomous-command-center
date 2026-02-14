# 🚀 Master Guide: All AI Providers, Free APIs & Zero-Auth Endpoints

> **Complete catalog of 349 AI providers, automated free-tier aggregation (~1.51 Billion monthly free tokens), zero-login endpoints, and auto-testing benchmarks.**

---

## 📊 Executive Summary & Catalog Statistics

| Metric | Count / Volume | Description |
| :--- | :--- | :--- |
| **Total Catalog Providers** | **349 Providers** | Comprehensive catalog spanning LLMs, Multimodal, Search, Audio, Video, and Cloud Agents. |
| **Local Configured Providers** | **125 Unique Providers** | Active connections detected on this machine in OmniRoute. |
| **Total Active Connections** | **168 Connections** | API Keys, OAuth tokens, and credential bridges active locally. |
| **Documented Steady Free Quota** | **~1.51 Billion tokens / month** | Across 42 deduped free-tier recurring pools. |
| **First-Month with Signup Credits**| **~2.13 Billion tokens** | Steady quota combined with one-time testing grants. |
| **Zero-Auth (No Login) Providers** | **11+ Providers** | Open public endpoints requiring no sign-in, key, or credit card. |
| **Permanently Free Uncapped Providers**| **6 Major Ecosystems** | SiliconFlow, Z.AI/Zhipu GLM-4-Flash, Baidu ERNIE, Tencent Hunyuan, Kilo, OpenCode. |

---

## 📑 Deliverables Index in Workspace

| File | Purpose |
| :--- | :--- |
| [`ALL_PROVIDERS_ARRANGED.txt`](./ALL_PROVIDERS_ARRANGED.txt) | **Master arranged text directory** of all 349 providers with IDs, aliases, categories, local connection statuses, free limits, notes, and websites. |
| [`NO_AUTH_ZERO_LOGIN_APIS.md`](./NO_AUTH_ZERO_LOGIN_APIS.md) | **Deep dive on Zero-Auth APIs**: Endpoint URLs, request/response formats, curl commands, and Python/Node.js snippets. |
| [`PROMPTS_AND_SETUP.md`](./PROMPTS_AND_SETUP.md) | **Production-ready prompts & integration**: Token-compressed system prompt, tool-calling emulator, strict JSON parser, and universal router. |
| [`test_free_apis.py`](./test_free_apis.py) | **Automated live testing script**: Pings endpoints, measures latency, validates responses, and outputs JSON benchmarks. |
| [`test_results.json`](./test_results.json) | **Live benchmark data**: Machine-readable latency and status output from automated probe runs. |

---

## 🏆 Part 1: The Zero-Auth / No-Login AI Tier

These providers require **no sign-up, no credit card, and no API key**. You can query them immediately from any client or shell.

```
+-----------------------------------------------------------------------------------------+
|                                 ZERO-AUTH AI WORKFLOW                                   |
|                                                                                         |
|   Client Script / cURL ----> Direct HTTP / WebSocket ----> Public Zero-Auth Provider   |
|                                                                 |                       |
|           +-----------------------------------------------------+                       |
|           |                                                                             |
|           +--> Pollinations AI   : Text (openai-fast), Vision, Image (Flux/SDXL)        |
|           +--> OpenCode Free     : Kimi K2.5, GLM-4.7, Qwen 2.5 Coder, MiniMax         |
|           +--> AI Horde          : Distributed volunteer GPU cluster (Key: 0000000000)  |
|           +--> DuckDuckGo Chat   : GPT-4o mini, Claude 3 Haiku, Llama 3.3 70B           |
|           +--> Jina Reader       : Semantic markdown web extraction (r.jina.ai)         |
|           +--> Cloudflare Play   : DeepSeek V3, Kimi K2.7, GLM 5.2, gpt-oss-120B        |
+-----------------------------------------------------------------------------------------+
```

### Detailed Provider Profiles:

#### 1. Pollinations AI
- **Endpoints**:
  - Direct Text GET: `https://text.pollinations.ai/{prompt}`
  - OpenAI Wire POST: `https://text.pollinations.ai/openai/chat/completions`
  - Image Generation: `https://image.pollinations.ai/prompt/{prompt}`
- **Models**: `openai-fast` (OVH reasoning), `mistral`, `qwen`, `flux`
- **Cost / Limits**: 100% Free, community-supported, best-effort rate limits.

#### 2. OpenCode Free (`opencode`)
- **Base URL**: `https://opencode.ai/zen/v1`
- **Models**: `kimi-k2.5`, `glm-4.7-flash`, `qwen2.5-coder-32b`, `mimo-v2.5`
- **Auth**: No key required (public free endpoint).

#### 3. AI Horde (`aihorde`)
- **Base URL**: `https://aihorde.net/api/v2`
- **Auth**: Documented anonymous key `0000000000`.
- **Models**: Crowdsourced Llama 3.3 70B, Cydonia 24B, Skyfall 31B, Stable Diffusion XL.
- **Mechanism**: Queued job submission with volunteer worker fulfillment.

#### 4. DuckDuckGo AI Chat (`duckduckgo-web`)
- **Website**: `https://duckduckgo.com/duckchat`
- **Models**: GPT-4o mini, Claude 3 Haiku, Llama 3.3 70B, Mixtral 8x7B.
- **Privacy**: No logging, anonymous sessions.

#### 5. Jina Reader (`jina-reader`)
- **Endpoint**: `https://r.jina.ai/{URL}`
- **Function**: Converts any public URL into pristine markdown for LLM context.
- **Rate Limit**: 20 requests per minute without any API key.

---

## 💎 Part 2: Permanently Free & Uncapped Providers

These providers provide **real recurring access with no published monthly token budget ceiling**. They are rate-limited by requests-per-minute (RPM) rather than a monthly hard stop.

| Provider | Access Mechanism | Notable Free Models | Published Limits / Quotas |
| :--- | :--- | :--- | :--- |
| **Groq** | Free API Key | `llama-3.3-70b-versatile`, `gemma2-9b-it`, `whisper-large-v3` | 30 RPM / 14,400 RPD on 8B; 1,000 RPD on 70B |
| **Google Gemini (AI Studio)**| Free API Key | `gemini-2.5-flash`, `gemini-3.1-flash-lite`, `gemma-3` | 15 RPM / 1,500 RPD (pooled Flash family) |
| **Mistral AI** | Free Experiment Tier | `mistral-small-2603`, `codestral`, `pixtral` | 2 RPM, 500k TPM, ~1 Billion tokens/month |
| **Cerebras Inference** | Free API Key | `llama-3.3-70b-instruct`, `gpt-oss-120b` | 5 RPM, 30k TPM, 1,000,000 tokens/day (~30M/mo) |
| **SambaNova Cloud** | Free API Key | `llama-3.3-70b`, `deepseek-r1-distill-llama-70b` | 20 RPM, 20 RPD, 200k tokens/day (~6M/mo) |
| **SiliconFlow** | Free API Key | `Qwen3-8B`, `DeepSeek-V3`, `GLM-4-9B` | Free $0 models permanently available |
| **Z.AI / Zhipu (GLM-CN)** | Free API Key | `glm-4-flash`, `glm-4.5-flash`, `glm-4.7-flash` | Permanently free + 20M signup bonus |
| **Baidu Qianfan** | Free API Key | `ernie-speed`, `ernie-lite`, `ernie-tiny` | Permanently free across multiple context lengths |
| **Cloudflare Workers AI** | Free API Key | `llama-3.3-70b`, `deepseek-r1`, `whisper` | 10,000 Neurons/day (~30M tokens/month) |

---

## 📈 Part 3: Quantified Recurring Monthly Free Token Pools

Top providers offering explicit monthly or daily token grants, calculated on steady recurring budgets:

```
+-----------------------------------------------------------------------------------------+
|                  TOP RECURRING MONTHLY FREE TOKEN GRANTS (STEADY BUDGET)                 |
|                                                                                         |
|   Mistral AI          : [==================================================] ~1.00B/mo  |
|   LLM7.io             : [=======] ~150M/mo                                              |
|   Google Gemini Flash : [===] ~60M/mo                                                   |
|   Cerebras Inference  : [=] ~30M/mo                                                     |
|   Cloudflare AI       : [=] ~30M/mo                                                     |
|   Api.airforce        : [=] ~24M/mo                                                     |
|   Ollama Cloud        : [=] ~20M/mo                                                     |
|   Groq (8B/70B)       : [=] ~15M/mo                                                     |
|   BluesMinds          : [-] ~7.2M/mo                                                    |
|   SambaNova Cloud     : [-] ~6M/mo                                                      |
|   Arcee AI            : [-] ~4.8M/mo                                                    |
|   BazaarLink          : [-] ~3.6M/mo                                                    |
|   OpenRouter (:free)  : [-] ~1M/mo                                                      |
+-----------------------------------------------------------------------------------------+
```

---

## 🎁 Part 4: High-Value Free Signup Credits & Grants

Generous one-time grants provided upon account creation (no credit card required for most):

| Provider | Free Signup Grant | Supported Models | Expiry / Notes |
| :--- | :--- | :--- | :--- |
| **FreeModel.dev** | **$300 free credits** | OpenAI GPT-5.4, GPT-5.5 via OpenAI API | No credit card required on signup |
| **AgentRouter** | **$100 - $200 free credits** | Claude Opus 4.8, Claude Opus 5, GPT-5.6 Sol | Multi-model routing gateway |
| **Pioneer AI** | **$75 free usage credits** | Frontier LLMs & reasoning engines | No card required |
| **Baseten** | **$30 GPU inference credits**| Dedicated serverless open models | 30-day trial period |
| **Together AI** | **$25 free starter credit** | Llama 3.3, Mixtral, FLUX, DeepSeek | Active developer community |
| **Inception Labs** | **10 Million free tokens** | Inception-family long context models | No card required |
| **Sarvam AI** | **₹1,000 INR credits** | Indic language LLMs, Audio, Speech | Never expires |
| **DeepSeek** | **5 Million free tokens** | DeepSeek V3, DeepSeek R1 reasoning | 30-day validity |
| **Scaleway AI** | **1 Million free tokens** | Qwen 2.5 72B, Llama 3.3 70B (Paris DC) | EU/GDPR compliant |
| **Fireworks AI** | **$1.00 starter credits** | Ultra-fast Llama 3.3, Qwen, DeepSeek | Developer evaluation |
| **Novita AI** | **$0.50 starter credits** | Video generation & LLM endpoints | 1-year validity |

---

## 🔍 Part 5: Free Multimodal, Vision & Search APIs

### 1. Web Search & Document Retrieval (RAG)
- **Exa Search (`exa-search`)**: 1,000 free searches/month. Embeddings-based neural search.
- **Tavily Search (`tavily-search`)**: 1,000 free searches/month. Tailored for LLM agents.
- **Firecrawl (`firecrawl`)**: 1,000 free crawl credits/month. Converts full web domains to clean markdown.
- **You.com Search (`youcom-search`)**: Free trial API key for web search.

### 2. Audio & Speech (TTS / STT)
- **Speechmatics (`speechmatics`)**: 8 hours/month permanently free. Industry-leading speech-to-text.
- **HuggingFace Inference API**: Free community inference for Whisper Large v3, VITS, and Bark.
- **Groq Whisper**: Free audio transcription with sub-second processing.

### 3. Image & Video Generation
- **Pollinations AI**: Free Flux.1 and SDXL image generation via simple GET URLs.
- **Veo AI Free**: Free short video generation (6 req/hour per IP).
- **Novita AI**: Video and image generation trial credits.

---

## 🌐 Part 6: Additional Free Providers Discovered (Beyond Catalog)

1. **GitHub Models / Azure AI Studio**:
   - Access directly through your GitHub account (`gh` CLI or Azure AI Studio).
   - Grants free daily quotas for **GPT-4o, GPT-4o mini, Claude 3.5 Sonnet, Llama 3.3 70B, and Phi-4**.
   - Zero billing setup required; authenticated via standard GitHub Personal Access Token (PAT).
2. **Cloudflare AI Gateway**:
   - Free unified reverse proxy providing universal caching, rate limiting, and analytics across all providers.
3. **Cohere Trial Platform**:
   - 1,000 free calls/month for `Command R+`, `Embed 3 English/Multilingual`, and `Rerank 3`.

---

## 🧪 Part 7: Live Automated Benchmark Results

Generated live by `test_free_apis.py` on this machine:

| Endpoint Target | Type | HTTP Status | Response Latency | Result & Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Pollinations AI (Text GET)** | No-Auth LLM | `200 OK` | **0.43s** | `[PASS]` Instant generation |
| **Jina Reader (Web Fetch)** | Web-to-Markdown | `200 OK` | **0.37s** | `[PASS]` Semantic markdown converted |
| **AI Horde Heartbeat** | No-Auth Cluster | `200 OK` | **0.22s** | `[PASS]` 25 active worker threads |
| **Cloudflare AI Playground** | No-Auth Web | `200 OK` | **0.09s** | `[PASS]` Ultra-fast CDN response |
| **DuckDuckGo DuckChat Web** | No-Auth Chat | `200 OK` | **1.82s** | `[PASS]` Handshake operational |
| **OmniRoute Local Proxy** | Local Gateway | `HTTP 401`* | **3.42s** | Gateway online (*requires auth key) |

*To authenticate with local OmniRoute, pass header `Authorization: Bearer sk-758f8a18f54de764-6fdf9d-dd10e9a6`.*

---

## 🛠️ Part 8: How to Route Everything Through OmniRoute

Your local OmniRoute instance runs at: `http://localhost:20128`
Dashboard URL: `http://localhost:20128/dashboard/providers`

### Example cURL Request to Local Gateway:
```bash
curl -X POST http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-758f8a18f54de764-6fdf9d-dd10e9a6" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto:free",
    "messages": [
      {"role": "user", "content": "Recommend the top 3 open-weight models in 2026."}
    ]
  }'
```

### Automatic Fallback Chain:
When querying `auto:free`:
1. OmniRoute tries **Groq (Llama 3.3 70B)** (sub-second latency).
2. If rate-limited (429), it immediately cascades to **Google Gemini 2.5 Flash**.
3. If quota exhausted, cascades to **Cerebras / SambaNova**.
4. If upstream cloud errors occur, cascades to **OpenCode Free / Pollinations AI**.

You get uninterrupted, 100% automated, zero-cost AI inference.

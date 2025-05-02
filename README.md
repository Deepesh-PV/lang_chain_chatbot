# 🏎️ Draggy — Your F1 AI Chatbot

**Draggy** is an F1-obsessed AI chatbot powered by **LLaMA 4**, delivering real-time updates, quirky commentary, and schedule insights. It combines:
- 🔍 **Tavily Search** for fresh F1 news
- 📆 **Custom F1 Schedule Tool** to keep you updated on upcoming races
- 🧠 **LLaMA 4** for Grok-style, personality-rich responses

---

## 🏁 Features

- **Live F1 News** via Tavily Search
- **F1 Schedule Checker** — When's the next Grand Prix?
- **Grok-Style Personality** — Think of it as your snarky F1-obsessed friend
- **Powered by LLaMA 4** for context-rich reasoning and fun banter

---

## ⚙️ Tech Stack

- 🧠 **LLaMA 4** (via Ollama, API, or custom server)
- 🔍 **Tavily Search API** for real-time answers
- 📆 **Custom F1 Schedule Tool** (YAML/JSON or API-backed)
- 🛠️ Python backend (LangChain or custom orchestration)
- (Optional) React / Streamlit frontend

---

## 📦 Setup

```bash
git clone https://github.com/yourusername/lang_chain_chatbot.git
cd draggy-f1-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 🇳🇬 NaijaTalk AI

<div align="center">

![NaijaTalk AI Banner](https://img.shields.io/badge/NaijaTalk-AI-green?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

**Nigeria's first AI chatbot that speaks, thinks, and responds in Nigerian Pidgin English!**

*E go answer you for Pidgin, e go even talk am back to you!* 🔊

[Live Demo](#) • [Report Bug](https://github.com/Santandave961/naijatalk-ai/issues) • [Request Feature](https://github.com/Santandave961/naijatalk-ai/issues)

</div>

---

## 📖 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Nigerian Pidgin Guide](#nigerian-pidgin-guide)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Author](#author)

---

## 🎯 About The Project

NaijaTalk AI is Nigeria's first AI-powered conversational chatbot that communicates exclusively in **Nigerian Pidgin English** — and speaks every response aloud using text-to-speech technology.

### The Problem
Most AI assistants like ChatGPT and Gemini respond only in formal English. But over **75 million Nigerians** communicate primarily in Pidgin English — a rich, expressive creole language that bridges Nigeria's 500+ ethnic groups. These Nigerians are underserved by existing AI tools.

### The Solution
NaijaTalk AI brings AI to the streets of Nigeria — responding in the language of the people, with the warmth and humor that Pidgin is known for. Whether you ask about technology, tell it your problems, or just want a laugh — e go answer you proper proper!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗣️ **Pidgin Only** | Every response is in authentic Nigerian Pidgin — no standard English |
| 🔊 **Text-to-Speech** | Auto-plays every response with Nigerian accent (gTTS com.ng) |
| 💬 **Full Conversation** | Maintains complete chat history across the session |
| ⚡ **Quick Prompts** | One-click buttons for instant conversation starters |
| 🎨 **Dark UI** | Clean, modern dark interface with Nigerian flag colors |
| 🔒 **Secure** | API key stays in browser — never stored or committed |
| 📱 **Responsive** | Works on desktop, tablet and mobile browsers |
| 🆓 **100% Free** | Powered by Gemini Flash free tier |

---

## 🎬 Demo

### Try These Phrases:

| English | What NaijaTalk Says |
|---------|---------------------|
| "How are you?" | "I dey fine well well! How you dey too?" |
| "What is AI?" | "AI na computer wey sabi think like human being..." |
| "Tell me a joke" | "Oya hear this one wey go make you laugh..." |
| "I need help" | "Abeg talk wetin dey do you, I dey here for you!" |
| "What is the weather?" | "Omo, I no fit check weather but make you look outside!" |

---

## 🛠️ Tech Stack

### Core Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Backend language | 3.9+ |
| **Streamlit** | Web application framework | Latest |
| **Google Gemini 1.5 Flash** | Pidgin language generation | API |
| **gTTS (Google Text-to-Speech)** | Voice synthesis with Nigerian accent | 2.5.4 |
| **google-genai** | Official Gemini Python SDK | Latest |

### Why These Technologies?

- **Gemini Flash** — Fast, free, and excellent at understanding context for creative language tasks like Pidgin generation
- **gTTS with `tld=com.ng`** — Uses Google's Nigerian English voice model for authentic accent
- **Streamlit** — Fastest way to deploy ML/AI apps with beautiful UI

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key (free at [aistudio.google.com](https://aistudio.google.com))
- Internet connection

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Santandave961/naijatalk-ai.git
cd naijatalk-ai
```

**2. Install dependencies**
```bash
pip install streamlit google-genai gtts
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Get your free API key**
- Go to [aistudio.google.com](https://aistudio.google.com)
- Click **"Get API Key"** → **"Create API Key"**
- Copy the key (starts with `AIza...`)
- Paste it in the app sidebar

**5. Start chatting!**
- Type any message or click a quick prompt button
- NaijaTalk AI will respond in Pidgin AND speak it aloud!

---

## ⚙️ How It Works

```
User Input (English/Pidgin/Any Language)
          ↓
    Google Gemini API
    (System Prompt: Respond ONLY in Nigerian Pidgin)
          ↓
    Pidgin Text Response
          ↓
    gTTS Text-to-Speech
    (lang="en", tld="com.ng" → Nigerian accent)
          ↓
    Audio Auto-plays in Browser
          ↓
    Text + Audio displayed in Chat UI
```

### The Pidgin System Prompt

The magic behind NaijaTalk AI is a carefully crafted system prompt that instructs Gemini to:
- Always respond in Nigerian Pidgin regardless of input language
- Use authentic Pidgin vocabulary (dey, wetin, abeg, wahala, oya, sabi)
- Maintain a warm, funny, Naija personality
- Keep responses concise for better TTS experience

---

## 🗣️ Nigerian Pidgin Guide

### Common Pidgin Words Used

| Pidgin | English Meaning |
|--------|----------------|
| I dey | I am / I'm here |
| Wetin | What |
| Abeg | Please |
| Wahala | Trouble / Problem |
| No wahala | No problem |
| Oya | Come on / Let's go |
| Sabi | Know / Understand |
| E don set | It's perfect / ready |
| Na so | That's right |
| Chop | Eat |
| Ginger | Motivate / Excite |
| E don do | It's finished |

---

## 📁 Project Structure

```
naijatalk-ai/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
└── .streamlit/
    └── secrets.toml      # API keys (NOT committed to git)
```

---

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"**
4. Select `Santandave961/naijatalk-ai` → `main` → `app.py`
5. Click **"Advanced settings"** and add:
```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```
6. Click **"Deploy"**

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |

---

## 🗺️ Roadmap

- [ ] Add voice input (speak to NaijaTalk, it replies in Pidgin)
- [ ] Add Igbo, Yoruba and Hausa language options
- [ ] WhatsApp integration
- [ ] Mobile app version
- [ ] Offline mode with local model

---

## 🤝 Contributing

Contributions are welcome! If you're Nigerian and want to improve the Pidgin quality:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/better-pidgin`)
3. Commit your changes (`git commit -m 'Add more authentic Pidgin phrases'`)
4. Push to the branch (`git push origin feature/better-pidgin`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Wisdom Okparaji**
*Data Scientist & ML Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-Santandave961-black?style=flat&logo=github)](https://github.com/Santandave961)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wisdom_Okparaji-blue?style=flat&logo=linkedin)](https://linkedin.com/in/wisdom-okparaji-680550246)
[![Twitter](https://img.shields.io/badge/X-@WOkparaji74619-black?style=flat&logo=x)](https://x.com/WOkparaji74619)
[![Portfolio](https://img.shields.io/badge/Portfolio-santandave961.github.io-green?style=flat)](https://santandave961.github.io)

---

## 🙏 Acknowledgements

- [Google Gemini](https://deepmind.google/technologies/gemini/) for the AI backbone
- [gTTS](https://gtts.readthedocs.io/) for Nigerian accent TTS
- [Streamlit](https://streamlit.io/) for the amazing app framework
- Every Nigerian who speaks Pidgin — una inspire this project! 🇳🇬

---

<div align="center">

**If this project resonates with you, abeg give am a ⭐ on GitHub!**

*Na Naija we dey, na Pidgin we sabi!* 🇳🇬

</div>

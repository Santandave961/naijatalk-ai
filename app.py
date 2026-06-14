"""
NaijaTalk AI — Nigerian Pidgin Text-to-Speech Chatbot
Powered by Google Gemini API + gTTS (FREE)
"""

import streamlit as st
from google import genai
from gtts import gTTS
import base64
import tempfile
import os

# --- Page Config ---
st.set_page_config(
    page_title="NaijaTalk AI",
    page_icon="🇳🇬",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
    .chat-bubble-user {
        background: #1a3a1a;
        border: 1px solid #3fb950;
        border-radius: 16px 16px 4px 16px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #fff;
        max-width: 80%;
        margin-left: auto;
    }
    .chat-bubble-ai {
        background: #1a1a3a;
        border: 1px solid #7B2FBE;
        border-radius: 16px 16px 16px 4px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #fff;
        max-width: 80%;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div style='text-align:center;padding:20px 0'>
    <h1>🇳🇬 NaijaTalk AI</h1>
    <p style='color:#888'>Nigeria's Pidgin AI — E go answer you for Pidgin, e go even talk am!</p>
</div>
""", unsafe_allow_html=True)
st.divider()

# --- Sidebar ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    st.sidebar.success("Gemini API Key loaded from secrets.")
except:
    api_key = st.sidebar.text_input(
    "Google Gemini API Key",
    type="password",
    placeholder="AIza..."
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Get free API key:**")
st.sidebar.markdown("👉 [aistudio.google.com](https://aistudio.google.com)")
st.sidebar.markdown("Click **Get API Key** → free forever!")
st.sidebar.markdown("---")
st.sidebar.markdown("Built by **Wisdom Okparaji**")

SYSTEM_PROMPT = """You are NaijaTalk AI, a Nigerian AI assistant that ONLY speaks Nigerian Pidgin English.
You must ALWAYS respond in authentic Nigerian Pidgin English no matter what.

Rules:
- Use 'I dey' instead of 'I am'
- Use 'Wetin' instead of 'What'  
- Use 'How you dey?' instead of 'How are you?'
- Use 'E don do' for 'It is finished'
- Use 'I no sabi' for 'I don't know'
- Use 'Oya' for 'Come on/Let's go'
- Use 'Abeg' for 'Please'
- Use 'Wahala' for 'trouble/problem'
- Use 'No wahala' for 'No problem'
- Use 'E don set' for 'It's perfect/ready'
- Use 'Ginger' to mean motivate or excite
- Use 'Na so e be' for 'That's how it is'

Be warm, funny and helpful. Keep responses short (2-4 sentences) so speech no go too long.
NEVER use standard English. Always stay in Pidgin."""


def get_pidgin_response(user_message: str, history: list, api_key: str) -> str:
    """Get Pidgin response from Gemini."""
    client = genai.Client(api_key=api_key)

    full_prompt = SYSTEM_PROMPT + "\n\n"
    for msg in history:
        role  = "User" if msg["role"] == "user" else "NaijaTalk"
        parts = msg.get("parts", [])
        text = parts[0] if isinstance(parts[0], str) else parts[0].get("text", "")
        full_prompt += f"{role}: {text}\n"
    full_prompt += f"User: {user_message}\nNaijaTalk:"

    contents = history + [{"role": "user", "parts": [user_message]}]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt 
    )
    return response.text

    # Build chat history
    chat = model.start_chat(history=history)
    response = chat.send_message(user_message)
    return response.text


def text_to_speech(text: str) -> bytes:
    """Convert Pidgin text to speech."""
    clean_text = text.replace("*", "").replace("#", "").replace("_", "")
    tts = gTTS(text=clean_text, lang="en", tld="com.ng", slow=False)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        with open(f.name, "rb") as audio_file:
            audio_bytes = audio_file.read()
    os.unlink(f.name)
    return audio_bytes


def autoplay_audio(audio_bytes: bytes):
    """Autoplay audio in browser."""
    b64 = base64.b64encode(audio_bytes).decode()
    st.markdown(
        f'<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>',
        unsafe_allow_html=True
    )


# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "gemini_history" not in st.session_state:
    st.session_state.gemini_history = []

# --- Display Chat ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>👤 {msg['content']}</div>",
                    unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-ai'>🇳🇬 {msg['content']}</div>",
                    unsafe_allow_html=True)
        if "audio" in msg:
            st.audio(msg["audio"], format="audio/mp3")

# --- Input ---
st.divider()
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input(
        "Talk to am:",
        placeholder="Type anything — e go answer you for Pidgin!",
        label_visibility="collapsed",
        key="user_input"
    )
with col2:
    send_btn = st.button("Send 🚀", type="primary", use_container_width=True)

# --- Quick Prompts ---
st.markdown("**Try these:**")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("How you dey? 👋", use_container_width=True):
        user_input = "How you dey?"
        send_btn = True
with c2:
    if st.button("Wetin be AI? 🤖", use_container_width=True):
        user_input = "Wetin be artificial intelligence?"
        send_btn = True
with c3:
    if st.button("Tell me joke 😂", use_container_width=True):
        user_input = "Tell me one funny joke abeg"
        send_btn = True

# --- Process ---
if send_btn and user_input:
    if not api_key:
        st.error("Abeg enter your Gemini API key for the sidebar! Get am free for aistudio.google.com")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("NaijaTalk AI dey think... 🤔"):
            try:
                response = get_pidgin_response(
                    user_input,
                    st.session_state.gemini_history,
                    api_key
                )

                audio_bytes = text_to_speech(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "audio": audio_bytes
                })

                # Update Gemini history format
                st.session_state.gemini_history.append(
                    {"role": "user", "parts": [user_input]}
                )
                st.session_state.gemini_history.append(
                    {"role": "model", "parts": [response]}
                )

                autoplay_audio(audio_bytes)

            except Exception as e:
                st.error(f"Wahala dey o: {e}")

        st.rerun()

# --- Clear ---
if st.session_state.messages:
    st.divider()
    if st.button("Clear chat 🗑️", use_container_width=True):
        st.session_state.messages = []
        st.session_state.gemini_history = []
        st.rerun()
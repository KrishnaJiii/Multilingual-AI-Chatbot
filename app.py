# Setup
import streamlit as st
from chatbot import MultiLingualchatbot
from datetime import datetime

# Page title
st.title("🗺️ Multilingual Chatbot")

# -------------------- SESSION STATE INIT --------------------

if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.all_chats[st.session_state.current_chat_id] = []

# -------------------- SIDEBAR --------------------

with st.sidebar:
    language = st.selectbox(
        "🌐 Select Language",
        ["English", "Hindi", "Spanish", "French", "German", "Japanese", "Chinese", "Arabic"]
    )

    # New Chat Button
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.current_chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.session_state.all_chats[st.session_state.current_chat_id] = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 💬 Chat History")

    # Show previous chats
    for chat_id in reversed(list(st.session_state.all_chats.keys())):
        messages = st.session_state.all_chats[chat_id]

        if messages:
            preview = messages[0]["content"][:30]
        else:
            preview = "New Chat"

        is_current = chat_id == st.session_state.current_chat_id

        if st.button(
            f"{'👉' if is_current else '💭'} {preview}",
            key=chat_id,
            use_container_width=True
        ):
            st.session_state.current_chat_id = chat_id
            st.rerun()

# -------------------- CURRENT CHAT --------------------

current_messages = st.session_state.all_chats[st.session_state.current_chat_id]

# Display chat messages
for msg in current_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------- CHAT INPUT --------------------

if prompt := st.chat_input("Type your message..."):

    # Show user message immediately
    current_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Stream assistant response
    chatbot = MultiLingualchatbot()

    import time

    with st.chat_message("assistant"):
        container = st.container(height=400)  # keeps page stable
        text_placeholder = container.markdown("")

        streamed_text = ""

        for token in chatbot.chat_stream(prompt, language, current_messages):
            streamed_text += token
            text_placeholder.markdown(streamed_text)
            time.sleep(0.01)  


    # Save assistant message
    current_messages.append({
        "role": "assistant",
        "content": streamed_text
    })

    st.session_state.all_chats[st.session_state.current_chat_id] = current_messages


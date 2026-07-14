import streamlit as st

from rag.chat_engine import ChatEngine


st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Real Estate AI Assistant")

st.write(
    "Ask questions about projects, pricing, payment plans, possession dates and more."
)

# -----------------------
# Initialize Chat Engine
# -----------------------

if "chat" not in st.session_state:
    st.session_state.chat = ChatEngine()

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Clear Conversation
# -----------------------

if st.sidebar.button("🗑 Clear Conversation"):

    st.session_state.messages = []

    st.session_state.chat.clear_history()

    st.rerun()

# -----------------------
# Display Chat
# -----------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if message["role"] == "assistant":

            if "sources" in message:

                with st.expander("Sources"):

                    for source in message["sources"]:

                        st.write(source)

# -----------------------
# Chat Input
# -----------------------

question = st.chat_input(
    "Ask your real estate question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.write(question)

    result = st.session_state.chat.ask(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"]
        }
    )

    with st.chat_message("assistant"):

        st.write(result["answer"])

        with st.expander("Sources"):

            for source in result["sources"]:

                st.write(source)

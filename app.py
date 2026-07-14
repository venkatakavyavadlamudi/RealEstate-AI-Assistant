import streamlit as st

from rag.chat_engine import ChatEngine


st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide"
)
# -----------------------
# Login Session
# -----------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------
# Login Screen
# -----------------------

if not st.session_state.logged_in:

    st.title("🏠 Real Estate AI Assistant")

    st.subheader("Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid username or password.")

    st.stop()

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

st.sidebar.title("🏠 Real Estate AI Assistant")

st.sidebar.write(f"Welcome, {st.session_state.username}")

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.messages = []

    st.session_state.chat.clear_history()

    st.rerun()

st.sidebar.divider()
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

                        st.write("📄", source.get("source", "Unknown Document"))

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

                st.write("📄", source.get("source", "Unknown Document"))

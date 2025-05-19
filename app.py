
import streamlit as st
from streamlit_chat import message
import random
from src.chatbot import medical_chatbot


st.set_page_config(page_title='🤖 MediBot', layout='centered', page_icon='🤖')
# st.title("🤖 MediBot Chat AI")

# --- Tiêu đề gọn và sát mép trên ---

st.markdown(
    """
    <style>
        .custom-title {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            padding: 0;
        }
    </style>
    <div class="custom-title">🤖 MediBot Chat AI</div>
    """,
    unsafe_allow_html=True
)


# adding session state to each user session
session_id = random.randint(0, 100000)
# adding session_id to session state
if "session_id" not in st.session_state:
    st.session_state.session_id = session_id

# initial message
INIT_MESSAGE = {"role": "assistant",
                "content": "Xin chào! Bạn muốn biết gì về các bệnh lý trong Y học nào?"}


if "messages" not in st.session_state:
        st.session_state.messages = [INIT_MESSAGE]

def generate_response(input_text):
    output = medical_chatbot(user_query=input_text)
    return output

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
user_input = st.chat_input(placeholder="Your message ....", key="input")

# display user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    user_message = st.chat_message("user")
    user_message.write(user_input)

# Generate response
if st.session_state.messages[-1]["role"] != "assistant":
    response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    assistant_message = st.chat_message("assistant")
    assistant_message.write(response)

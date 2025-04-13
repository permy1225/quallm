import streamlit as st
import requests

st.title("QuaLLM with MCP")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("メッセージを入力してください"):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role", "user", "content", prompt})

    with st.chat_message("assistant"):
        with st.spinner("考え中..."):
            try:
                response = requests.post(
                    "http://quallm-backend:8000/chat",
                    json={"query": prompt}
                )
                if response.status_code == 200:
                    assistant_response = response.json()
                    st.write(assistant_response)
                    st.session_state.messages.append(
                        {"role", "assistant", "content", assistant_response}
                    )
                else:
                    st.error(f"エラーが発生しました: {response.status_code}")
            except Exception as e:
                st.error(f"エラーが発生しました: {str}")
    
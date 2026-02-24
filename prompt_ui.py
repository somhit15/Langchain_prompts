import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Research Assistant", page_icon="📚")



model = ChatNVIDIA(model_name="qwen/qwen3.5-397b-a17b")

st.title("📚 Research Assistant")
st.caption("Powering your literature review and data synthesis")

user_input = st.text_input("Ask a research question...")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)

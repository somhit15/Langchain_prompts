import streamlit as st
import time

st.set_page_config(page_title="Research Assistant", page_icon="📚")

st.title("📚 Research Assistant")
st.caption("Powering your literature review and data synthesis")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Research Assistant. How can I help you analyze papers or synthesize information today?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    st.selectbox("Model", ["GPT-4o", "Claude 3.5 Sonnet", "Llama 3"])
    st.file_uploader("Upload Research Papers (PDF)", accept_multiple_files=True)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# React to user input
if prompt := st.chat_input("Ask a research question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulated response logic
        assistant_response = f"I am analyzing your request regarding: '{prompt}'. In a production environment, I would now query your uploaded documents and provide cited answers."
        
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
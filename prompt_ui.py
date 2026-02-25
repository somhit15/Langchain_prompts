import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
load_dotenv()

st.set_page_config(page_title="Research Assistant", page_icon="📚")
st.title("📚 Research Assistant")
st.caption("Powering your literature review and data synthesis")



model = ChatNVIDIA(model_name="qwen/qwen3.5-397b-a17b")

paper_input = st.selectbox("Select Research paaper name",["Select ...", "Attention is all you need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "Generative Pre-trained Transformer 2 (GPT-2)", "Language Models are Few-Shot Learners", "Scaling Laws for Neural Language Models", "Deep Learning for Natural Language Processing"])

style_input = st.selectbox("Select style", ["Select ...", "Summarize", "Explain", "Compare", "Contrast", "Analyze", "Evaluate", "Critique", "Discuss", "Elaborate", "Expand", "Extend", "Generalize", "Illustrate", "Interpret", "Justify", "Outline", "Paraphrase", "Predict", "Propose", "Question", "Recommend", "Research", "Review", "Summarize", "Synthesize", "Translate"])

length_input = st.selectbox("Select Explanation length", ["Select ...", "Short", "Medium", "Long"])


# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}

    1. Mathematical Details:
        - Include relevant mathematical reference if present in the paper.
        - Explain the mathematical concepts using simple and intuitive code snippets where applicable.
        - Provide examples where applicable.

    2. Analogies:
        - Use real-world analogies to explain complex concepts.
        - Make the explanation intuitive and easy to understand.

    If certain information is not present in the paper, please respond with "Insufficient information available in the paper to provide the explanation." instead of hallucinating.

    Ensure the summary is clear, accurate and aligned with the user's request.
    """
)

prompt = prompt_template.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input})



if st.button("Submit"):
    result = model.invoke(prompt)
    st.write(result.content)

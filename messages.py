from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
load_dotenv()

model = ChatNVIDIA(
    model = "qwen/qwen3-next-80b-a3b-instruct")

system_msg = SystemMessage("""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

human_msg = HumanMessage("How do I create a REST API?")

messages = [system_msg, human_msg]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)



from langchain.chat_models import init_chat_model
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

#moonshotai/kimi-k2.5
#qwen/qwen3-next-80b-a3b-instruct

model = ChatNVIDIA(model = "Orion-zhen/Qwen2.5-7B-Instruct-Uncensored",
base_url="https://nim.api.nvidia.com/v1")

chat_history = []

while True:
    user_input = input("User : ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": result.content})
    print("AI : ", result.content)
    print('--------------------------------')

print("\n\n\n",chat_history)
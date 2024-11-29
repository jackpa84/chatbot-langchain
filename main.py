from langchain_core.messages import HumanMessage, SystemMessage
from langchain_cohere import ChatCohere
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from  decouple import config

COHERE_API_KEY = config("COHERE_API_KEY")

set_llm_cache(InMemoryCache())

# Defina as mensagens
system_message = SystemMessage(content="Você é um assistente útil e amigável.")
human_message = HumanMessage(content="Você entende português do Brasil?")

# Combine as mensagens em uma lista
messages = [system_message, human_message]

# Inicialize o modelo de chat da Cohere com a chave de API
chat_model = ChatCohere(cohere_api_key=COHERE_API_KEY)

for chunk in chat_model.stream(messages):
    print(chunk.content, end="", flush=True)
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from decouple import config
import json

class ChatView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        user_message = data.get('message', '')

        COHERE_API_KEY = config("COHERE_API_KEY")
        set_llm_cache(InMemoryCache())

        # Defina as mensagens
        system_message = SystemMessage(content="Você é um assistente útil e amigável.")
        human_message = HumanMessage(content=user_message)

        # Combine as mensagens em uma lista
        messages = [system_message, human_message]

        # Inicialize o modelo de chat da Cohere com a chave de API
        chat_model = ChatCohere(cohere_api_key=COHERE_API_KEY)

        def stream_response():
            for chunk in chat_model.stream(messages):
                yield chunk.content

        return StreamingHttpResponse(stream_response(), content_type='text/plain')

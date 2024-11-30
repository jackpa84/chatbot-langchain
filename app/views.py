import json
import logging

from decouple import config
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from langchain.globals import set_llm_cache
from langchain_cohere import ChatCohere
from langchain_community.cache import InMemoryCache
from langchain_core.messages import HumanMessage, SystemMessage

logging.basicConfig(level=logging.DEBUG)

COHERE_API_KEY = config("COHERE_API_KEY")

set_llm_cache(InMemoryCache())


def index(request):
    return render(request, 'chatbot/index.html')


@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_message = body.get('message', '')
        except json.JSONDecodeError:
            return JsonResponse({'response': 'Erro no formato da mensagem.'})

        if user_message:
            system_message = SystemMessage(content="Você é um assistente útil e amigável.")
            human_message = HumanMessage(content=user_message)
            messages = [system_message, human_message]

            chat_model = ChatCohere(cohere_api_key=COHERE_API_KEY)

            def stream_response():
                for chunk in chat_model.stream(messages):
                    yield chunk.content

            return StreamingHttpResponse(stream_response(), content_type="text/plain")
        return JsonResponse({'response': 'Desculpe, não entendi sua mensagem.'})
    return JsonResponse({'response': 'Método não permitido.'})

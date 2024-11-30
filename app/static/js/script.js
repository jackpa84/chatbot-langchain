document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');

    // Envia mensagem ao backend
    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const userMessage = messageInput.value.trim();
        if (!userMessage) return;

        appendMessage('user', userMessage);
        messageInput.value = '';
        streamMessageToBot(userMessage);
    });

    // Adiciona uma mensagem ao chat
    function appendMessage(sender, message, isStream = false) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');
        messageContent.textContent = message;

        messageElement.appendChild(messageContent);
        chatBox.appendChild(messageElement);

        chatBox.scrollTop = chatBox.scrollHeight;

        // Retorna o elemento para stream se necessário
        if (isStream) return messageContent;
    }

    // Função para fazer o stream da resposta do bot
    async function streamMessageToBot(message) {
        const responseElement = appendMessage('bot', '', true); // Cria o espaço para o stream

        try {
            const response = await fetch('/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error('Erro ao obter resposta do bot.');
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            let botMessage = '';
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value);
                botMessage += chunk;
                responseElement.textContent = botMessage; // Atualiza o texto do balão
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        } catch (error) {
            console.error('Erro:', error);
            responseElement.textContent = 'Desculpe, ocorreu um erro ao processar sua mensagem.';
        }
    }

    // Função para obter o token CSRF
    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const trimmedCookie = cookie.trim();
            if (trimmedCookie.startsWith(`${name}=`)) {
                return decodeURIComponent(trimmedCookie.split('=')[1]);
            }
        }
        return null;
    }
});


# Chatbot com LangChain e Cohere AI

Este projeto é um chatbot desenvolvido com Django que utiliza o LangChain e o modelo de linguagem da Cohere para interagir com os usuários de forma amigável e útil.

---

## **Tecnologias Utilizadas**

- **Python 3.12**
- **Django**
- **LangChain**
- **Cohere API**
- **LangChain-Cohere**
- **LangChain-OpenAI**
- **LangChain-Community**
- **Python-Decouple**
- **Numpy**

---

## **Como Adquirir uma Chave API na Cohere**

1. **Acesse o site da Cohere:** Visite [cohere.ai](https://cohere.ai).
2. **Crie uma conta ou faça login:**
   - Se ainda não tiver uma conta, clique em **Sign Up** e siga os passos para criar uma.
   - Caso já tenha, clique em **Login**.
3. **Obtenha sua chave API:**
   - Após o login, acesse o **Dashboard**.
   - Navegue até a seção **API Keys**.
   - Clique em **Create API Key** para gerar uma nova chave ou copie uma chave existente.
4. **Guarde a chave com segurança:** Sua chave API é sensível e deve ser mantida em segredo.

---

## **Como Instalar e Rodar a Aplicação**

### **Pré-requisitos**
- **Python 3.12** instalado.
- **Poetry** instalado. Caso não tenha, instale com:
  
    ```bash
    pip install poetry
    ```

- **Chave API da Cohere** obtida conforme instruções acima.

---

### **Instalação**

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd seu_repositorio
    ```

3. **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    poetry shell
    ```

4. **Instale as dependências com o Poetry:**

    ```bash
    poetry install
    ```

---

### **Configuração**

1. **Crie um arquivo `.env` na raiz do projeto.**
2. **Adicione as seguintes variáveis ao `.env`:**

    ```
    SECRET_KEY=sua-chave-secreta
    DEBUG=True
    COHERE_API_KEY=sua-chave-api-da-cohere
    ```

    - Substitua `sua-chave-secreta` por uma chave secreta de sua escolha (pode ser uma sequência aleatória de caracteres).
    - Substitua `sua-chave-api-da-cohere` pela chave API que você obteve da Cohere.

---

### **Executando a Aplicação**

1. **Aplique as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

2. **Inicie o servidor Django:**

    ```bash
    python manage.py runserver
    ```

3. **Acesse a aplicação em seu navegador:**

    ```arduino
    http://localhost:8000/
    ```

Agora, você pode interagir com o chatbot diretamente pela interface web.

---

## **Estrutura do Projeto**

```csharp
├── app
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── script.js
│   ├── templates
│   │   └── chatbot
│   │       └── index.html
│   ├── urls.py
│   └── views.py
├── chatbot_langchain
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main.py
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

## **Contato**

Em caso de dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Autor:** Jackson Pacheco  
- **Email:** [jackpa1984@gmail.com](mailto:jackpa1984@gmail.com)

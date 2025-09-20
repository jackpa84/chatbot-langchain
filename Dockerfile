FROM python:3.13-slim

# Opcional: dependências de sistema se precisar compilar algo
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential git && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install --upgrade pip && pip install poetry

WORKDIR /code

# Copia apenas os manifests para aproveitar cache de dependências
COPY pyproject.toml poetry.lock* ./

# Instala dependências sem instalar o pacote raiz (evita exigir README/código)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Agora copia o restante do código
COPY . .

# Se você realmente precisa instalar o projeto como pacote, faça depois que o código estiver copiado:
# RUN poetry install --no-interaction --no-ansi

# Ajuste conforme seu app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
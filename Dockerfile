FROM python:3.13-slim

# Proxy (opcional, útil em corp/VPN)
ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NO_PROXY
ENV http_proxy=${HTTP_PROXY} https_proxy=${HTTPS_PROXY} no_proxy=${NO_PROXY}

# Variáveis e boas práticas
ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

# Certificados e utilitários básicos
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl \
 && rm -rf /var/lib/apt/lists/*

# Atualiza pip e instala Poetry
RUN python -m pip install --upgrade --no-cache-dir pip \
 && pip install --no-cache-dir "poetry==${POETRY_VERSION}"

# Copia manifestos primeiro para aproveitar cache
COPY pyproject.toml poetry.lock* ./

# Instala dependências do projeto (sem criar venv)
RUN poetry install --no-ansi

# Copia o restante do código
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
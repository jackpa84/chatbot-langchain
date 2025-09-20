FROM python:13.3-slim

# Instala Poetry
RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /code

# Copia o pyproject.toml e o poetry.lock
COPY pyproject.toml poetry.lock* ./

# Instala dependências via Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o restante do projeto
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
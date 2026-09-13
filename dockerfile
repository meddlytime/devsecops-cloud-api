FROM python:3.12-alpine

# Criar um usuário sem privilégios de root por segurança
RUN adduser -D appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ajustar permissões e alternar para o usuário comum
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
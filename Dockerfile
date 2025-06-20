FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY user-prompt.py .
CMD ["uvicorn", "user-prompt:app", "--host", "0.0.0.0", "--port", "8000"]
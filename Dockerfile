FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Build-time metadata, injected by CI (git tag + commit SHA)
ARG APPLICATION_VERSION=0.0.0-local
ARG MODEL_VERSION=model-1
ARG GIT_COMMIT=unknown

ENV APPLICATION_VERSION=${APPLICATION_VERSION}
ENV MODEL_VERSION=${MODEL_VERSION}
ENV GIT_COMMIT=${GIT_COMMIT}

EXPOSE 5000
CMD ["python", "app.py"]

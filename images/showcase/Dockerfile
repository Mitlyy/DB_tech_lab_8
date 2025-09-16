FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash appuser
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r /app/requirements.txt

COPY app /app/app

EXPOSE 9000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=5 \
  CMD curl -fsS http://127.0.0.1:9000/health || exit 1

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]


# --- Builder stage ---
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv \
    && uv sync --frozen --no-dev --python=$(which python3)

COPY src/ ./src

# --- Final stage ---
FROM python:3.12-slim

# Install only runtime deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy prebuilt venv and app
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY entrypoint.sh /app/entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

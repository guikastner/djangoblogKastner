# syntax=docker/dockerfile:1
FROM python:3.14-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps for Pillow and runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -U pip && pip install -r requirements.txt

# Copy project
COPY . .

# Entrypoint
RUN chmod +x docker/entrypoint.sh

EXPOSE 8000
CMD ["/bin/sh", "docker/entrypoint.sh"]

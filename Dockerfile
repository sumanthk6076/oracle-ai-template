# ── BASE IMAGE ──
FROM python:3.11-slim

# ── METADATA ──
LABEL maintainer="your-email@example.com"
LABEL description="Oracle AI repo — GlobalManufacturing Corp"
LABEL oracle_version="23ai"

# ── WORKING DIRECTORY ──
WORKDIR /app

# ── SYSTEM DEPENDENCIES ──
# libaio1 is required by python-oracledb on Linux
RUN apt-get update \
    && apt-get install -y --no-install-recommends libaio1 \
    && rm -rf /var/lib/apt/lists/*

# ── PYTHON DEPENDENCIES ──
# Copy requirements first — Docker caches this layer
# Only re-runs pip install if requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── APPLICATION CODE ──
COPY src/ ./src/
COPY main.py .
COPY generate_fixtures.py .
COPY .env.example .

# ── WALLET ──
# NEVER bake wallet into image — mount at runtime
# Run command:
# docker run \
#   -v /path/to/wallet:/app/wallet \
#   --env-file .env \
#   oracle-ai-hello

# ── ENTRY POINT ──
CMD ["python", "main.py"]

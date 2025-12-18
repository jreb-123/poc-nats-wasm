FROM python:3.11-slim

# ===============================
# Dependencias del sistema (TODAS)
# ===============================
RUN apt update && apt install -y \
    curl \
    git \
    clang \
    lld \
    wasi-libc \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Instalar WasmEdge
# ===============================
RUN curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash

WORKDIR /app

# ===============================
# Compilar WASM
# ===============================
COPY processor.c .
RUN clang --target=wasm32-wasi processor.c -o wasm_processor.wasm

# ===============================
# Python
# ===============================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY subscriber.py .

CMD ["python", "subscriber.py"]

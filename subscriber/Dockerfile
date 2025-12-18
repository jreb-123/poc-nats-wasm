FROM python:3.11-slim

# Dependencias del sistema
RUN apt update && apt install -y \
    curl \
    clang \
    lld \
    wasi-libc \
    && rm -rf /var/lib/apt/lists/*

# Instalar WasmEdge
RUN curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash

WORKDIR /app

# Copiar WASM source (desde el contexto)
COPY processor.c .

# Compilar WASM
RUN clang --target=wasm32-wasi processor.c -o wasm_processor.wasm

# Python deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Código del subscriber
COPY subscriber.py .

CMD ["python", "subscriber.py"]

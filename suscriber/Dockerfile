FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt update && apt install -y \
    curl \
    clang \
    lld \
    wasi-libc \
    && rm -rf /var/lib/apt/lists/*

# Instalar WasmEdge
RUN curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash

WORKDIR /app

# Copiar WASM source
COPY wasm/processor.c /app/processor.c

# Compilar C → WASM
RUN clang --target=wasm32-wasi processor.c -o wasm_processor.wasm

# Python deps
COPY subscriber/requirements.txt .
RUN pip install -r requirements.txt

COPY subscriber/subscriber.py .

CMD ["python", "subscriber.py"]

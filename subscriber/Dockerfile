FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# ===============================
# Paquetes base
# ===============================
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    ca-certificates \
    build-essential \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Instalar WASI-SDK
# ===============================
WORKDIR /opt

RUN wget https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-20/wasi-sdk-20.0-linux.tar.gz && \
    tar xvf wasi-sdk-20.0-linux.tar.gz && \
    rm wasi-sdk-20.0-linux.tar.gz

ENV WASI_SDK_PATH=/opt/wasi-sdk-20.0
ENV PATH="${WASI_SDK_PATH}/bin:${PATH}"

# ===============================
# App
# ===============================
WORKDIR /app

COPY processor.c .

# ===============================
# Compilar a WASM
# ===============================
RUN clang \
    --target=wasm32-wasi \
    --sysroot=${WASI_SDK_PATH}/share/wasi-sysroot \
    processor.c \
    -o wasm_processor.wasm

CMD ["ls", "-lh", "wasm_processor.wasm"]


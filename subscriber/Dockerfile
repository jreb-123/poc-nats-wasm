FROM wasmedge/wasmedge:0.13.5

# ===============================
# Dependencias de compilación
# ===============================
RUN apt-get update && apt-get install -y \
    clang \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Instalar WASI-SDK (FIJO)
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

RUN clang \
    --target=wasm32-wasi \
    --sysroot=${WASI_SDK_PATH}/share/wasi-sysroot \
    processor.c \
    -o wasm_processor.wasm

# ===============================
# Ejecutar WASM
# ===============================
CMD ["wasmedge", "wasm_processor.wasm"]

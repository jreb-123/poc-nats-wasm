# ============================
# STAGE 1: Build WASM
# ============================
FROM ubuntu:22.04 AS wasm-builder

RUN apt-get update && apt-get install -y \
    clang \
    lld \
    wasi-libc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY processor.c .

RUN clang \
  --target=wasm32-wasi \
  --sysroot=/usr/share/wasi-sysroot \
  processor.c \
  -O3 \
  -o wasm_processor.wasm

# ============================
# STAGE 2: Runtime
# ============================
FROM wasmedge/slim:0.13.5

WORKDIR /app

COPY --from=wasm-builder /build/wasm_processor.wasm .

COPY subscriber.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["wasmedge", "wasm_processor.wasm"]

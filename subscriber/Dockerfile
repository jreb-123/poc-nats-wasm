# ---------- Builder ----------
  FROM ubuntu:22.04 AS wasm-builder

  RUN apt-get update && apt-get install -y \
      curl \
      xz-utils \
      build-essential \
      && rm -rf /var/lib/apt/lists/*
  
  # Install WASI SDK
  WORKDIR /opt
  RUN curl -L https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-20/wasi-sdk-20.0-linux.tar.gz \
      | tar xz
  
  ENV WASI_SDK_PATH=/opt/wasi-sdk-20.0
  ENV PATH="${WASI_SDK_PATH}/bin:${PATH}"
  
  WORKDIR /build
  COPY processor.c .
  
  RUN clang \
      --target=wasm32-wasi \
      processor.c \
      -O3 \
      -o wasm_processor.wasm
  
  # ---------- Runtime ----------
  FROM wasmedge/slim:0.13.5
  
  WORKDIR /app
  COPY --from=wasm-builder /build/wasm_processor.wasm .
  
  CMD ["wasmedge", "wasm_processor.wasm"]
  
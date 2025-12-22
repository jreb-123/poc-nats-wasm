FROM wasmedge/slim:0.13.5

WORKDIR /app

# Copiamos el wasm ya compilado
COPY wasm_processor.wasm .

# Ejecutamos el módulo WASM
CMD ["wasmedge", "wasm_processor.wasm"]

FROM wasmedge/wasmedge:0.13.5

WORKDIR /app

# Copiamos el WASM
COPY wasm_processor.wasm .

# Ejecutamos directamente wasmedge
CMD ["wasmedge", "wasm_processor.wasm"]

FROM wasmedge/slim:0.13.5

WORKDIR /app
COPY wasm_processor.wasm .

CMD ["wasmedge", "wasm_processor.wasm"]

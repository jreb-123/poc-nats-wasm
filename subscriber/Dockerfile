FROM wasmedge/slim:0.13.5

WORKDIR /app
COPY wasm_processor.wasm .

CMD ["sh", "-c", "wasmedge wasm_processor.wasm && sleep infinity"]

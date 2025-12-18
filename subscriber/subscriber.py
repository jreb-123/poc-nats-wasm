import asyncio
from nats.aio.client import Client as NATS
import subprocess

NATS_URL = "nats://nats.nats.svc.cluster.local:4222"

async def main():
    nc = NATS()
    await nc.connect(servers=[NATS_URL])

    async def handler(msg):
        data = msg.data.decode()
        print(f"Received: {data}")

        result = subprocess.run(
            ["wasmedge", "wasm_processor.wasm"],
            capture_output=True,
            text=True
        )
        print(result.stdout)

    await nc.subscribe("poc.events", cb=handler)

    while True:
        await asyncio.sleep(1)

asyncio.run(main())

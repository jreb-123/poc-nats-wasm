const { connect } = require("nats");

async function start() {
  const nc = await connect({
    servers: process.env.NATS_URL || "nats://nats.nats.svc.cluster.local:4222"
  });

  console.log("Connected to NATS");

  let counter = 0;

  setInterval(() => {
    const msg = `message-${counter}`;
    nc.publish("poc.events", Buffer.from(msg));
    console.log("Published:", msg);
    counter++;
  }, 3000);
}

start().catch(console.error);

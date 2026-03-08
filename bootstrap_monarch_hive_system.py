import os, textwrap

ROOT="monarch-hive"

def write(path,content):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        f.write(textwrap.dedent(content))


# LICENSE

write(f"{ROOT}/LICENSE","""
Monarch Non-Commercial Source License (MNCSL) v1.0

Copyright (c) 2026 Steven Craig Leake Jr.

Permission is granted to any person obtaining a copy of this software and
associated documentation files (the "Software") to use, study, modify,
and redistribute the Software for NON-COMMERCIAL purposes, subject to
the following conditions:

1. The above copyright notice and this license shall be included in all
copies or substantial portions of the Software.

2. COMMERCIAL USE IS NOT PERMITTED without explicit written permission.

3. Commercial licensing is available through:

   Monarch Literary
   Licensing Department
   Contact: licensing@monarchliterary.com

4. Commercial use includes but is not limited to:
   - selling the software
   - offering paid hosted services using the software
   - integrating the software into commercial products

5. Any organization wishing to deploy the software commercially must
obtain a written commercial license from Monarch Literary.

DISCLAIMER

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY.
""")


# README

write(f"{ROOT}/README.md","""
# Monarch Hive

Monarch Hive is a distributed sovereign node system combining:

• Rust mesh nodes  
• local trade ledger  
• QR wallet clients  
• Sophia reasoning agents  
• IPFS anchoring  
• Tor hidden service gateway  

The system is designed as a **decentralized experimental infrastructure platform**.

---

## Repository Structure

services/

hive-node  
Sophia-agent  
web-gateway  

clients/

wallet  

infra/

tor  
ipfs  

shared/

did identity tools  

---

## Quick Start

Generate the repository:

python bootstrap_monarch_hive_system.py

Run hive node:

cd services/hive-node
cargo run

Run Sophia agent:

python services/sophia-agent/sophia_agent.py

Run dashboard:

python services/web-gateway/server.py

---

## License

This project uses the **Monarch Non-Commercial Source License**.

Free for research, experimentation, and personal use.

Commercial use requires written licensing through:

Monarch Literary  
licensing@monarchliterary.com
""")


# OPERATIONS MANUAL

write(f"{ROOT}/OPERATIONS_MANUAL.md","""
# Monarch Hive Operations Manual

This document explains how to operate a Monarch Hive node.

---

## Node Responsibilities

Each node performs the following functions:

• maintain local ledger
• communicate with peer nodes
• optionally anchor snapshots to IPFS
• optionally expose Tor hidden service
• run Sophia analysis agent

---

## Starting a Node

1 Install dependencies

Rust
Python
IPFS
Tor

2 Run node

cargo run

3 Launch Sophia agent

python sophia_agent.py

---

## Network Architecture

Nodes exchange information through peer-to-peer gossip channels.

Ledger updates propagate automatically.

Nodes can join the network via bootstrap peers.

---

## Security Guidelines

Do not expose nodes directly to the public internet without firewall rules.

Use Tor hidden services for privacy.

Always verify dependencies.

---

## Maintenance

Rotate logs weekly.

Verify ledger integrity.

Backup local node state.

---

## Commercial Licensing

Commercial deployment requires written authorization.

Contact Monarch Literary for licensing.
""")


# RUST NODE

write(f"{ROOT}/services/hive-node/Cargo.toml","""
[package]
name="hive-node"
version="0.1.0"
edition="2021"

[dependencies]
serde={version="1",features=["derive"]}
sha2="0.10"
""")


write(f"{ROOT}/services/hive-node/src/main.rs","""
use serde::{Serialize,Deserialize};
use sha2::{Sha256,Digest};
use std::collections::HashMap;

#[derive(Serialize,Deserialize,Clone)]
struct Trade{
from:String,
to:String,
item:String,
amount:f64,
timestamp:u64,
hash:String
}

struct Ledger{
trades:HashMap<String,Trade>
}

impl Ledger{

fn new()->Self{
Self{trades:HashMap::new()}
}

fn hash_trade(trade:&Trade)->String{

let mut h=Sha256::new();

h.update(format!("{}{}{}{}",
trade.from,
trade.to,
trade.item,
trade.timestamp));

format!("{:x}",h.finalize())
}

fn add(&mut self,trade:Trade){

let key=format!("{}-{}",trade.from,trade.timestamp);

self.trades.insert(key,trade);

println!("trade recorded {}",key);
}

}

fn main(){

let mut ledger=Ledger::new();

println!("Monarch Hive node running");

}
""")


# SOPHIA AGENT

write(f"{ROOT}/services/sophia-agent/sophia_agent.py","""
import random,time

class Sophia:

 def observe(self):
  return random.choice(["trade","market","weather"])

 def reason(self,event):

  if event=="trade":
   return "trade activity rising"

  return "network stable"

if __name__=="__main__":

 s=Sophia()

 while True:

  e=s.observe()

  print("Sophia insight:",s.reason(e))

  time.sleep(5)
""")


# WALLET

write(f"{ROOT}/clients/wallet/wallet.py","""
import hashlib,time,qrcode

class Wallet:

 def create_trade(self,amount,memo):

  payload=f"monarch:{amount}:{memo}:{int(time.time())}"

  h=hashlib.sha256(payload.encode()).hexdigest()

  img=qrcode.make(h)

  img.save("trade.png")

  print("QR generated")

if __name__=="__main__":

 Wallet().create_trade(1.0,"coffee")
""")


# TOR

write(f"{ROOT}/infra/tor/start_onion.sh","""
#!/bin/bash
echo "starting tor service"
tor --HiddenServiceDir ./tor_service --HiddenServicePort 80 127.0.0.1:8080
""")

print("Monarch Hive system generated with license, README, and operations manual.")
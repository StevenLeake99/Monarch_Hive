
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

# Adaptive Edge Offloading using Deep Reinforcement Learning

This project simulates a learning-based edge computing environment for energy-aware task offloading in future 6G networks. The agent decides whether to process tasks locally or offload them to the cloud, based on dynamic factors such as battery level, network condition, and data importance.

## 🔍 Features
- Deep Q-Learning based offloading agent  
- Simulated energy–latency–accuracy tradeoffs  
- Trust-aware and value-driven decision logic  
- Easily extendable for research and experimentation  

## 🧠 Architecture
The agent observes a 3D state:
- **Battery level**
- **Network latency**
- **Task importance**

Two actions:  
- `0`: Local execution  
- `1`: Offload to server  

The environment returns a reward balancing energy, delay, and task value.

## ⚙️ Installation
```bash
git clone https://github.com/Reza-ebi/adaptive-edge-offloading
cd adaptive-edge-offloading
pip install -r requirements.txt

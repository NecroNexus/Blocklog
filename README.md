🔐 BlockLog – Blockchain-Based Immutable Logging System
📌 Abstract

BlockLog is a blockchain-based logging system that ensures log integrity and immutability using Ethereum smart contracts.
Instead of storing raw logs on-chain, the system stores cryptographic hashes of logs, making any tampering or modification easily detectable.

This project demonstrates a real-world cybersecurity application of blockchain in secure auditing, forensics, and compliance systems.

🎯 Objective

The objectives of this project are:

To prevent unauthorized modification of logs

To ensure immutability of security audit records

To demonstrate blockchain usage in cybersecurity

To apply cryptographic hashing for log integrity

❗ Problem Statement

Traditional centralized logging systems have several security weaknesses:

Logs can be modified or deleted by attackers

Insider threats can manipulate audit trails

No cryptographic proof of authenticity

Centralized log servers are single points of failure

In cybersecurity and digital forensics, logs must be trustworthy and tamper-proof.

💡 Proposed Solution

BlockLog uses blockchain technology to solve these issues:

Log messages are hashed using keccak256

Only hashes are stored on the blockchain

Blockchain ensures immutability and transparency

Any modification changes the hash and exposes tampering

🧠 Technologies & Concepts Used

Blockchain Technology

Ethereum Smart Contracts

Solidity

Cryptographic Hashing (keccak256)

Hardhat Development Framework

Ethers.js

Local Ethereum Network

🏗️ System Architecture

System / Application Logs
→ Hash Generation (keccak256)
→ Ethereum Smart Contract
→ Immutable Blockchain Storage

📁 Project Structure

blockchain/
├── contracts/
│ └── BlockLog.sol
├── scripts/
│ ├── deploy.js
│ └── addLog.js
├── hardhat.config.js
├── package.json
├── package-lock.json
├── README.md
└── .gitignore

📜 Smart Contract Description
Contract: BlockLog.sol

Each log entry contains:

logHash – Hash of the log message

timestamp – Time of log creation

logger – Ethereum address of the sender

Why Hash-Based Storage?

Sensitive data is not exposed

Lower gas cost

Better privacy

Scalable design

🚀 Installation & Execution Steps
Step 1: Install dependencies

npm install

Step 2: Compile the smart contract

npx hardhat compile

Step 3: Start local blockchain

npx hardhat node

Step 4: Deploy the smart contract

npx hardhat run scripts/deploy.js --network localhost

Step 5: Add a log entry

npx hardhat run scripts/addLog.js --network localhost

🧪 Sample Output

BlockLog deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3
Log added to blockchain
Log message: User login from IP 10.0.0.1
Log hash: 0x0e20775bc6058d5c31bddcbb943934ab9681883ce71ed64c37fcce59a7bbddb

🔐 Security Advantages

Tamper-proof logging

Immutable audit trails

Insider attack resistance

Trustless verification

Useful for SOC, compliance, and forensic analysis

const hre = require("hardhat");

async function main() {
const CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

const BlockLog = await hre.ethers.getContractFactory("BlockLog");
const blockLog = await BlockLog.attach(CONTRACT_ADDRESS);

const count = await blockLog.totalLogs();
console.log(`📦 Total logs on blockchain: ${count}`);

for (let i = 0; i < count; i++) {
    const log = await blockLog.getLog(i);
    console.log(`\n🧾 Log #${i}`);
    console.log("Hash      :", log[0]);
    console.log("Timestamp :", new Date(Number(log[1]) * 1000).toISOString());
    console.log("Logger    :", log[2]);
}
}

main().catch(console.error);
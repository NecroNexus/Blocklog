const hre = require("hardhat");
const { ethers } = hre;

async function main() {
const CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

  // Attach to deployed contract
const BlockLog = await ethers.getContractFactory("BlockLog");
const blockLog = await BlockLog.attach(CONTRACT_ADDRESS);

  // Example log message
const logMessage = "User login from IP 10.0.0.1";

  // Hash the log (this is what we store on-chain)
const logHash = ethers.utils.keccak256(
    ethers.utils.toUtf8Bytes(logMessage)
);

const tx = await blockLog.addLog(logHash);
await tx.wait();

console.log("✅ Log added to blockchain");
console.log("Log message:", logMessage);
console.log("Log hash:", logHash);
}

main().catch((error) => {
console.error(error);
process.exit(1);
});
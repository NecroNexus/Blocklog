const hre = require("hardhat");

async function main() {
const BlockLog = await hre.ethers.getContractFactory("BlockLog");
const blockLog = await BlockLog.deploy();

await blockLog.deployed();

console.log("✅ BlockLog deployed to:", blockLog.address);
}

main().catch((error) => {
console.error(error);
process.exit(1);
});
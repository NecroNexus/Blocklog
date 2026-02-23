import time
from web3 import Web3
from eth_account import Account
from datetime import datetime

# ===== BLOCKCHAIN CONFIG =====
RPC_URL = "http://127.0.0.1:8545"

# Hardhat Account #0 private key (safe for local demo)
PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

# 🔴 REPLACE WITH YOUR DEPLOYED CONTRACT ADDRESS
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# ABI (only required function)
CONTRACT_ABI = [
{
"inputs": [{"internalType": "bytes32", "name": "_logHash", "type": "bytes32"}],
"name": "addLog",
"outputs": [],
"stateMutability": "nonpayable",
"type": "function",
}
]

# ===== WEB3 SETUP =====
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(PRIVATE_KEY)
contract = w3.eth.contract(
address=Web3.to_checksum_address(CONTRACT_ADDRESS),
abi=CONTRACT_ABI
)

print("🚀 Python Blockchain Logger Started")
print("Connected account:", account.address)

# ===== AUTOMATIC LOG GENERATOR =====
ACTIONS = [
"USER_LOGIN",
"FILE_ACCESSED",
"FAILED_LOGIN_ATTEMPT",
"CONFIG_CHANGED",
"ADMIN_LOGIN"
]

def generate_log(action):
    timestamp = datetime.utcnow().isoformat()
    return f"Action: {action} | Time: {timestamp}"

# ===== MAIN LOOP =====
while True:
    try:
        action = ACTIONS[int(time.time()) % len(ACTIONS)]
        log_message = generate_log(action)

        # Hash log (keccak256)
        log_hash = w3.keccak(text=log_message)

        nonce = w3.eth.get_transaction_count(account.address)

        txn = contract.functions.addLog(log_hash).build_transaction({
            "from": account.address,
            "nonce": nonce,
            "gas": 300000,
            "gasPrice": w3.to_wei("20", "gwei"),
        })

        signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

        print("✅ Log stored on blockchain")
        print("   Log:", log_message)
        print("   Hash:", log_hash.hex())
        print("   Tx:", tx_hash.hex())
        print("-" * 60)

        time.sleep(5)  # generate log every 5 seconds

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(5)
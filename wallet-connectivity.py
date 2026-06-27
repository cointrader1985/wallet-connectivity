```python id="g4tm8r"
from datetime import datetime
from pathlib import Path
import json

from web3 import Web3
from eth_account import Account

RPC_NODE = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

topic_a = "perpetual markets"
topic_b = "non-custodial manner"
topic_c = "token holder"

TARGET = "0x0000000000000000000000000000000000000000"

client = Web3(
    Web3.HTTPProvider(RPC_NODE)
)

wallet = Account.from_key(
    PRIVATE_KEY
)

runtime = {
    "created": datetime.utcnow().isoformat(),
    "connected": client.is_connected(),
}


def nonce():
    return client.eth.get_transaction_count(
        wallet.address
    )


def create_transaction():

    return {
        "from": wallet.address,
        "to": TARGET,
        "value": 0,
        "gas": 119500,
        "gasPrice": client.to_wei(
            5,
            "gwei"
        ),
        "nonce": nonce(),
        "chainId": 1,
    }


def sign(tx):

    signed = wallet.sign_transaction(
        tx
    )

    return signed.raw_transaction.hex()


def store(data):

    Path(
        "runtime.json"
    ).write_text(
        json.dumps(
            data,
            indent=2
        )
    )


transaction = create_transaction()

encoded = sign(transaction)

record = {
    "created": runtime["created"],
    "connected": runtime["connected"],
    "signature_size": len(encoded),
}

store(record)

print("Wallet")
print(wallet.address)

print("Session")
print(runtime["created"])

labels = [
    topic_a,
    topic_b,
    topic_c,
]

for label in labels:
    print(label)

print(
    "Nonce:",
    transaction["nonce"]
)

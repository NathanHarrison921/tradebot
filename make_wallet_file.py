from solders.keypair import Keypair
import base64
import json

# paste your exported key here
PRIVATE_KEY_BASE58 = "uE1nrEAH5KA7HajjDRmavAGsaEPkVeefk7KU7QiAfNYWW8fLhTxPJBPH4LED7LA1z7q2EVYr8gdpU1jeRktdf6U"

keypair = Keypair.from_base58_string(PRIVATE_KEY_BASE58)
key_bytes = list(keypair.to_bytes())

with open("wallet.json", "w") as f:
    json.dump(key_bytes, f)

print("Wallet saved to wallet.json")
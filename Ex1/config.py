from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

# TODO: Fill this in with your private key.
# 私钥
my_private_key = CBitcoinSecret(
    'cQvAwbiURvrbjaVHVyNMiyWQgUvHwMcdgTitsKvcJMYUZkNUZjnc')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

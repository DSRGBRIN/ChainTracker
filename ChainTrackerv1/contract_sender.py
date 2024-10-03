"""
Module komunikasi dengan blockchain smart contract
"""
import time
import sys
from web3 import Web3
# from web3.middleware_onion import geth_poa_middleware
# from web3.middleware_onion import async_geth_poa_middleware
from abi_code import TRACK_ABI

NET_ID = {"polygon": 137, "celo": 42220}
NET_URL = {"polygon": "https://polygon-mainnet.infura.io/v3/4ae814529fcf43ddb3eec654d77c5578",
           "celo": "https://celo-mainnet.infura.io/v3/4ae814529fcf43ddb3eec654d77c5578"}


def call_data(network, sc_adr, sc_abi, param, ret=False):
    """
    get contract data
    """
    print(network, sc_adr, param)
    w3 = Web3(Web3.HTTPProvider(NET_URL[network]))
    # w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # myAdr = owner["account"]
    # private_key = owner["accountKey"]

    # abi = ABI
    contract_adr = Web3.to_checksum_address(sc_adr)
    the_contract = w3.eth.contract(address=contract_adr, abi=sc_abi)

    ret_data = the_contract.functions.data(param).call()
    print(ret_data, type(ret_data))
    if ret:
        return ret_data


def test(network, pk_sender):
    """
    send transaction to call a contract function
    """
    w3 = Web3(Web3.HTTPProvider(NET_URL[network]))
    nonce = w3.eth.get_transaction_count(pk_sender)
    nonce2 = w3.eth.get_transaction_count(pk_sender, 'pending')
    print(nonce, nonce2)


def call_tracking(network, sc_adr, sc_abi, pk_sender, sk_sender, param):
    """
    send transaction to call a contract function
    """

    w3 = Web3(Web3.HTTPProvider(NET_URL[network]))
    # w3.middleware_onion.inject(async_geth_poa_middleware, layer=0)

    # myAdr = owner["account"]
    # private_key = owner["accountKey"]
    nonce = w3.eth.get_transaction_count(pk_sender)
    # nonce2 = w3.eth.get_transaction_count(pk_sender, 'pending')
    # print(nonce, nonce2)
    # return

    # abi = ABI
    contract_adr = Web3.to_checksum_address(sc_adr)
    the_contract = w3.eth.contract(address=contract_adr, abi=sc_abi)

    transaction = {
        'from': pk_sender,
        'value': 0,
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price,  # w3.to_wei('41', 'gwei'),
        'nonce': nonce,
        'chainId': NET_ID[network]
    }

    print(network, sc_adr, pk_sender, sk_sender, nonce)
    print(param)

    deploy_txn = the_contract.functions.track(param[0], param[1]).build_transaction(transaction)
    signed_txn = w3.eth.account.sign_transaction(deploy_txn, private_key=sk_sender)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(txn_hash.hex())
    # tx = w3.eth.get_transaction(txn_hash)
    # assert tx["from"] == pk_sender
    return txn_hash.hex()


if __name__ == "__main__":
    P_ADR = "0xeCE741E83a69ee075ECdd223e2AE6B26805B4D30"
    C_ADR = "0x2807fe5aff1b0EE81108D8295631a61fDA80037f"

    U_ADR = "0x9073e1dc12f0f44E1af024D00e047990Dd7a9e76"
    U_KEY = "2df21f58103f990a96eab0409b102f850cef477b295d5e2d943279377606e644"
    IPFS_URL = "testing only"

    MODE = int(sys.argv[1])
    bc_network = sys.argv[2]  # celo or polygon
    if bc_network == "celo":
        S_ADR = C_ADR
    elif bc_network == "polygon":
        S_ADR = P_ADR
    if MODE == 0:
        # T_NOW = 479737
        T_NOW = int(sys.argv[3])
        call_data(bc_network, S_ADR, TRACK_ABI, T_NOW)
    else:
        T_NOW = int(time.time())//3600
        print(T_NOW)
        param_function = []
        param_function.append(str(T_NOW))
        param_function.append(IPFS_URL)
        call_tracking(bc_network, S_ADR, TRACK_ABI, U_ADR, U_KEY, param_function)

from web3 import Web3
import bsure_abi
URL = 'https://kovan.infura.io/v3/4b7137f3af3f4c18873a5837bbd7c0ba'
token_in = '0x706cd8eb2ba08bc2b26d2789c11a225dc8689aea'
bsure_address = '0x56775CDa4C21358D57280432b41AED65702e2Df5'

user_address = '0x701123a676E9A765191276C1587c01b009646EF6'
#wallet_privateKey = ''
# Connect to Blockchain
def ProviderConnect():
    w3 = Web3(Web3.HTTPProvider(URL))
    return w3

# Connect to Blockchain with wallet
def WalletConnect(provider):
    account = provider.eth.accounts.privateKeyToAccount('0x' + wallet_privateKey);
    provider.eth.accounts.wallet.add(account);
    provider.eth.defaultAccount = account.address;
    return true

# Prepare contract to make calls
def LoadContract(provider, address, abi):
    contract_instance = provider.eth.contract(address=address, abi=abi)
    return contract_instance

# Call getStorageId() contract function
def StorageId(contract, address):
    storage_id = contract.functions.getStorageId(address).call()
    return storage_id

# Call getStorageId() contract function
def StorageInfo(contract, _id):
    storage_info = contract.functions.getInfo(_id).call()
    return storage_info

# Make Transaction Deposit_plan_1() contract function
def try_Deposit_plan_1(contract):
    tx_hash = contract.functions.Deposit_plan_1().transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Make Transaction Deposit_plan_2() contract function
def try_Deposit_plan_2(contract):
    tx_hash = contract.functions.Deposit_plan_2().transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Make Transaction withdrawVault() contract function
def try_withdrawVault(contract):
    tx_hash = contract.functions.withdrawVault().transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Make Transaction withdrawVault() contract function
def try_reinvestVault(contract):
    tx_hash = contract.functions.reinvestVault().transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Make connection to blockchain without wallet (ONLY CALL FUNCTIONS)
provider = ProviderConnect()
# Connect to contract without wallet
get_bsure_contract = LoadContract(provider, bsure_address, bsure_abi.bsure_abi)
# Check last block number
print(provider.eth.block_number)
# Get storage id for user
check_id = StorageId(get_bsure_contract, user_address)
print(check_id)
# Get Info for id
print(StorageInfo(get_bsure_contract, check_id))

# Make connection to blockchain with wallet (ONLY CALL FUNCTIONS)
#WalletConnect(provider)

#print(try_Deposit_plan_1(get_bsure_contract))

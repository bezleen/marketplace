from scripts.helper import get_account
from brownie import accounts, config, SaturnMarketPlace
from web3 import Web3


def a():
    deploy_account = get_account()
    account = get_account(index=1)
    current_contract = SaturnMarketPlace.deploy({"from": deploy_account})
    print(f"Contract deployed to {current_contract.address}")
    current_contract.createNFTOnMarket("http://localhost", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)


def b():
    deploy_account = get_account()
    current_contract = SaturnMarketPlace.deploy({"from": deploy_account})
    print(f"Contract deployed to {current_contract.address}")
    account = get_account(index=1)
    current_contract.createMyNFT("http://localhost", {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost123213123", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost1232131234", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost12321312345", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(account)
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)
    # next
    account = get_account(index=2)
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(account)
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)


def c():
    deploy_account = get_account()
    current_contract = SaturnMarketPlace.deploy({"from": deploy_account})
    print(f"Contract deployed to {current_contract.address}")
    account = get_account(index=1)
    current_contract.createMyNFT("http://localhost", {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost123213123", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost1232131234", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost12321312345", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(f"before: {account}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)
    # act
    current_contract.sellNFT(1, Web3.toWei(0.000002, 'ether'), {"from": account, "value": 25000000000})
    ######
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(f"after: {account}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)


def d():
    deploy_account = get_account()
    current_contract = SaturnMarketPlace.deploy({"from": deploy_account})
    print(f"Contract deployed to {current_contract.address}")
    account = get_account(index=1)
    current_contract.createMyNFT("http://localhost", {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost123213123", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost1232131234", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    current_contract.createNFTOnMarket("http://localhost12321312345", Web3.toWei(0.000001, 'ether'), {"from": account, "value": 25000000000})
    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(f"1.1: {account}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)

    account2 = get_account(index=2)
    all_items_listed = current_contract.getListedItems({"from": account2})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account2})
    #
    all_my_nft = current_contract.getMyItems({"from": account2})
    print(f"2.1: {account2}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)
    current_contract.purchaseNFT(2, {"from": account2, "value": Web3.toWei(0.000001, 'ether')})

    all_items_listed = current_contract.getListedItems({"from": account})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account})
    #
    all_my_nft = current_contract.getMyItems({"from": account})
    print(f"2.1: {account}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)

    all_items_listed = current_contract.getListedItems({"from": account2})
    #
    all_my_items_listed = current_contract.getMyListedItems({"from": account2})
    #
    all_my_nft = current_contract.getMyItems({"from": account2})
    print(f"2.2: {account2}")
    print("all_items_listed")
    print(all_items_listed)
    print("all_my_items_listed")
    print(all_my_items_listed)
    print("all_my_nft")
    print(all_my_nft)


def main():
    d()

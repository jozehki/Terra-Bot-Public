from terra_sdk.client.lcd import LCDClient
from terra_sdk.key.mnemonic import MnemonicKey
import time
import datetime

MILLION = 1000000

""" VARIABLES TO UPDATE ACCORDING TO THE NEW NFT MINT IN LUART """
minting_price = 89
nft_mint_contract = 'terra1zfacfuel6ys0p89j3w6qyn0e5nrhccv496rdap'
mint_count = 3 # number of mints per transaction

public_mint_time = "2022/04/30 00:00:00" # this is their stated time, not your local time
send_tx_count = 3 # number of transaction to spam when bot trigger
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def terra_lcd():
    return LCDClient("https://lcd.terra.dev", "columbus-5")

def wallet_info():
    terra = terra_lcd()
    seed_phrase = "ENTER YOUR SEED PHRASE HERE"
    mk = MnemonicKey(mnemonic=(seed_phrase))
    wallet = terra.wallet(mk)
    account_number = wallet.account_number()
    return wallet, account_number

def mint_info():
    luart_minting_fee = 0.2
    total_mint_cost = int((minting_price + luart_minting_fee) * MILLION)
    return total_mint_cost, mint_count, nft_mint_contract, send_tx_count

def check_time():
    mint_time = int(time.mktime(datetime.datetime.strptime(public_mint_time, "%Y/%m/%d %H:%M:%S").timetuple()))
    timenow = int(time.mktime(datetime.datetime.now().timetuple()))
    return mint_time, timenow

from config import terra_lcd, wallet_info, mint_info, check_time
from luart import LuartExecute
from time import sleep

execute = LuartExecute(terra_lcd(), wallet_info()[0], wallet_info()[1])

def generate_mint_msg():
    mint_count = mint_info()[1]
    msges = []
    msg = execute.random_mint(mint_info()[2], mint_info()[0])
    for count in range(mint_count): # Number of Mint per Tx
        msges.append(msg)
    return msges

def trigger_mint(msg):
    sequence = execute.getSequence()
    send_tx_count = mint_info()[3]
    for count in range(send_tx_count): # Number of Tx send when Trigger
        print(f"\n#{count + 1} Broadcast")
        execute.broadcast_tx(msg, sequence)
        sequence += 1
    exit()

def check_mint_time():
    if check_time()[1] > check_time()[0]:
        print(f"\nTime for Public Sale Reached")
        print(f"Start Mint Broadcast")
        msg = generate_mint_msg()
        trigger_mint(msg)

def main():
    print(f"\nStarting Countdown")
    while 1:
        check_mint_time()
        sleep(1) # in seconds

main()

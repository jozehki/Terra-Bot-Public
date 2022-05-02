from terra_sdk.core.wasm import MsgExecuteContract

class LuartExecute:
    ust_gas = "0.15001uusd"
    gas_adj = 1.6

    def __init__(self, terra, wallet, acc_num):
        self.terra = terra
        self.wallet = wallet
        self.acc_num = acc_num

    def getSequence(self):
        return self.wallet.sequence()

    def random_mint(self, contract_addr, amount):
        msg = MsgExecuteContract(
            self.wallet.key.acc_address,
            contract_addr,
            {
                "random_mint": {}
            },
            {'uusd': str(amount)},
        )
        return msg

    def broadcast_tx(self, msg, seq):
        tx = self.wallet.create_and_sign_tx(CreateTxOptions(msgs=msg, gas_prices=self.ust_gas, gas_adjustment=self.gas_adj, account_number=self.acc_num, sequence=seq))
        result = self.terra.tx.broadcast_sync(tx)
        print(result.txhash)

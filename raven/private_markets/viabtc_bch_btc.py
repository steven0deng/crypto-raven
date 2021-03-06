# Copyright (C) 2017, Philsong <songbohr@gmail.com>

from ._viabtc import Viabtc

class PrivateViabtc_BCH_BTC(Viabtc):
    def __init__(self):
        super().__init__("BTC", "BCH", "bccbtc")

    def test(self):
        # balance = self.get_balances()

        order_id = self.buy_limit(0.01, 0.02)
        print(order_id)
        order_status = self.get_order(order_id)
        print(order_status)
        # balance = self.get_balances()

        cancel_status = self.cancel_order(order_id)
        print(cancel_status)
        order_status = self.get_order(order_id)
        print(order_status)

        # balance = self.get_balances()

        order_id = self.sell_limit(0.01, 50000)
        print(order_id)
        order_status = self.get_order(order_id)
        print(order_status)

        # balance = self.get_balances()

        cancel_status = self.cancel_order(order_id)
        print(cancel_status)
        order_status = self.get_order(order_id)
        print(order_status)


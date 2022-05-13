from decimal import Decimal


class BitbankTransaction:
    chain = "bitbank"

    def __init__(self, transaction: dict):
        self.transaction = transaction

    def get_transaction_from_data(self) -> dict:
        return self.transaction

    def get_data_type(self) -> str:
        return self.transaction["data_type"]

    def get_datetime_jtc(self) -> str:
        return self.transaction["取引日時"]

    def get_transaction_id(self) -> str:
        return self.transaction["取引ID"]

    def get_token_pair(self) -> str:
        return self.transaction["通貨ペア"]

    def get_amount(self) -> Decimal:
        return Decimal(self.transaction["数量"])

    def get_price(self) -> Decimal:
        return Decimal(self.transaction["価格"])

    def get_fee(self) -> Decimal:
        return Decimal(self.transaction["手数料"])

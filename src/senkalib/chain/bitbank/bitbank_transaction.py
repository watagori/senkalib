class BitbankTransaction:
    chain = "bitbank"

    def __init__(self, transaction: dict):
        self.transaction = transaction

    def get_transaction(self) -> dict:
        return self.transaction

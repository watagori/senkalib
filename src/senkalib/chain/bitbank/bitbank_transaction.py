class BitbankTransaction:
    chain = "bitbank"

    def __init__(self, transaction: dict):
        self.transaction = transaction

    def get_transaction(self) -> dict:
        return self.transaction

    def get_transaction_data_type(self) -> str:
        return self.transaction["data_type"]

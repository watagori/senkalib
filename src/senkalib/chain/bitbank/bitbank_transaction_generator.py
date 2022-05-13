from typing import List

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transactions_from_data(
        cls,
        settings: SenkaSetting,
        data: dict,
    ) -> List[BitbankTransaction]:
        return list(map(lambda x: BitbankTransactionGenerator._add_data_type(x), data))

    @staticmethod
    def _add_data_type(data: dict) -> BitbankTransaction:
        data["data_type"] == "bitbankc_exchange"
        return BitbankTransaction(data)

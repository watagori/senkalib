from typing import List

from senkalib.chain.bitbank.bitbank_transaction import BitbankTransaction
from senkalib.chain.transaction import Transaction
from senkalib.chain.transaction_generator import TransactionGenerator
from senkalib.senka_setting import SenkaSetting


class BitbankTransactionGenerator(TransactionGenerator):
    chain = "bitbank"

    @classmethod
    def get_transactions_from_data(
            cls,
            settings: SenkaSetting,
            data: dict,
    ) -> List[Transaction]:
        return list(
            map(
                BitbankTransaction,
                data
            )
        )

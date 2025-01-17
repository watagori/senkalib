import asyncio
from typing import List, Union

from bscscan import BscScan
from web3 import Web3

from senkalib.chain.bsc.bsc_transaction import BscTransaction
from senkalib.chain.transaction import Transaction
from senkalib.chain.transaction_generator import TransactionGenerator


class BscTransactionGenerator(TransactionGenerator):
    chain = "bsc"

    @classmethod
    def get_transactions(cls, transaction_params: dict) -> List[Transaction]:
        settings_bsc = transaction_params["settings"].get_settings()
        startblock = (
            transaction_params["startblock"]
            if transaction_params["startblock"] is not None
            else 0
        )
        endblock = (
            transaction_params["endblock"]
            if transaction_params["endblock"] is not None
            else None
        )
        w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
        transactions = []

        page = 1
        while True:
            txs = asyncio.run(
                BscTransactionGenerator.get_txs(
                    settings_bsc,
                    transaction_params["data"],
                    startblock,
                    endblock,
                    page,
                )
            )
            for tx in txs:
                if "1" in tx["isError"]:
                    continue
                else:
                    receipt = w3.eth.get_transaction_receipt(tx["hash"])
                    transactions.append(
                        BscTransaction(
                            tx["hash"],
                            receipt,
                            tx["timeStamp"],
                            tx["gasUsed"],
                            tx["gasPrice"],
                        )
                    )

            page += 1
            if len(txs) < 10000:  # bscscan api return 10000 results for each page
                break

        return transactions

    @classmethod
    async def get_txs(
        cls,
        settings: dict,
        address: str,
        arg_startblock: Union[int, None] = None,
        arg_endblock: Union[int, None] = None,
        arg_page: Union[int, None] = None,
    ):
        async with BscScan(settings["bscscan_key"]) as bscscan:
            txs = await bscscan.get_normal_txs_by_address_paginated(
                address=address,
                startblock=arg_startblock,
                endblock=arg_endblock,
                page=arg_page,
                offset=0,
                sort="asc",
            )

        return txs

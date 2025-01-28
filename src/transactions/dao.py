from src.dao.base import BaseDAO
from src.transactions.models import Transactions


class TransactionsDAO(BaseDAO):
    """"""
    model = Transactions

    @classmethod
    async def add(cls):
        """"""
        pass

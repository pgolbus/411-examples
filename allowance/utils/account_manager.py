from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime

import sqlite3
import pytz

from . import logger

logger = logger.get_logger(__name__)

@dataclass
class Transaction:
    amount: float
    type: int  # -1 = withdrawal, 0 = not cool, 1 = deposit, 2 = super cool
    description: str

@dataclass
class DateTransaction:
    date: str
    description: str
    amount: float
    type: int


@contextmanager
def get_db_connection():
    logger.info("getting db connection")
    conn = sqlite3.connect('/home/pgolbus/repos/allowance/transactions.db')
    logger.debug("connection: %s", conn)
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def get_balance():
    logger.info("getting balance")
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # first we need to get the most recent Not Cool and start counting from there
        cursor.execute('SELECT MAX(id) FROM transactions WHERE type = 0 AND deleted = 0;')
        not_cool_id = cursor.fetchone()[0]
        not_cool_id = not_cool_id if not_cool_id is not None else 0
        cursor.execute(f'SELECT SUM(amount * type) FROM transactions WHERE deleted = 0 AND id >= {not_cool_id};')
        balance = cursor.fetchone()[0]
        logger.info("balance: %s", balance)
        return balance

def get_not_cools():
    logger.info("getting not cools")
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(CASE WHEN type = 0 THEN -1 WHEN type = 2 THEN 1 ELSE 0 END) FROM transactions WHERE deleted = 0;')
        not_cools = cursor.fetchone()[0]
        logger.info("not cools: %s", not_cools)
        return not_cools


def get_boston_time():
    boston = pytz.timezone('America/New_York')
    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Make it timezone-aware
    utc_now = utc_now.replace(tzinfo=pytz.utc)

    # Convert to Boston time
    boston_now = utc_now.astimezone(boston)

    # Format the time
    formatted_time = boston_now.strftime("%Y-%m-%d%l:%M:%S %p")
    return formatted_time

def get_transactions():
    logger.info("getting transactions")
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT date, description, amount, type FROM transactions WHERE deleted = 0 ORDER BY id DESC;')
        transactions = cursor.fetchall()
        logger.debug("transactions: %s", transactions)
        return [DateTransaction(*transaction) for transaction in transactions]

def delete_transaction(date):
    logger.info("deleting transaction from %s" % date)
    delete_query = f"""UPDATE transactions SET deleted = 1 WHERE date = '{date}';"""
    logger.debug("delete query: %s", delete_query)
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(delete_query)

def enter_transaction(transaction):
    logger.info(f"Entering transacion: {transaction.amount}, {transaction.type}, {transaction.description}")
    insert_query = f"""insert into transactions (date, amount, type, description)
        VALUES ('{get_boston_time()}',
        {transaction.amount},
        '{transaction.type}',
        '{transaction.description}');
        """
    logger.debug("insert query: %s", insert_query)
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(insert_query)

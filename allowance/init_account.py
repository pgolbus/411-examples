import click

from utils import account_manager, logger

logger = logger.get_logger(__name__)

create_table_query = """CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    type INTEGER NOT NULL,
    description TEXT,
    deleted INTEGER NOT NULL DEFAULT 0
)
"""

drop_table_query = """DROP TABLE IF EXISTS transactions"""

@click.command()
@click.option("--balance", default=0, type=float, help="Initial balance")
def main(balance):
    if balance < 0:
        raise ValueError("Initial balance cannot be negative")
    if (balance * 100) % 1 != 0:
        raise ValueError("Initial balance cannot include fractions of cents")
    with account_manager.get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(drop_table_query)
        cursor.execute(create_table_query)
    intial_transaction = account_manager.Transaction(balance, "deposit", "Initializing transaction")
    account_manager.enter_transaction(intial_transaction)
    balance = account_manager.get_balance()
    logger.info("Table createed with initial balance: %s", balance)

if __name__ == "__main__":
    main()
import os

from dotenv import load_dotenv

from utils import account_manager, logger

load_dotenv()

logger = logger.get_logger(__name__)


def main():
    try:
        patreon = float(os.getenv("PATREON"))
        logger.info("Starting patreon: %s" % patreon)
        balance = account_manager.get_balance()
        logger.info("Starting balance: %s" % balance)
        transaction = account_manager.Transaction(patreon, -1, "Patreon")
        account_manager.enter_transaction(transaction)
        balance = account_manager.get_balance()
        logger.info("Updated balance :%s" % balance)
    except Exception as e:
        logger.error(e)
        raise e

if __name__=="__main__":
    main()

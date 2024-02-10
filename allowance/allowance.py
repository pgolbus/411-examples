import os

from dotenv import load_dotenv

from utils import account_manager, logger

load_dotenv()

logger = logger.get_logger(__name__)


def main():
    try:
        allowance = float(os.getenv("ALLOWANCE"))
        logger.info("Starting weekly allowance: %s" % allowance)
        balance = account_manager.get_balance()
        logger.info("Starting balance: %s" % balance)
        transaction = account_manager.Transaction(allowance, 1, "Weekly allowance")
        account_manager.enter_transaction(transaction)
        balance = account_manager.get_balance()
        logger.info("Updated balance :%s" % balance)
    except Exception as e:
        logger.error(e)
        raise e

if __name__=="__main__":
    main()

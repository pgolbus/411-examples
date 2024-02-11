import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from utils import account_manager


app = Flask(__name__)
app.logger.setLevel('INFO')


# injects the contents of the .env file into the OS environment
load_dotenv()

@app.route('/healthcheck')
def healthcheck():
    return 'OK', 200

@app.route('/')
def index():
    app.logger.info('Page accessed')
    app.logger.debug('Getting balance')
    balance = account_manager.get_balance()
    cools = account_manager.get_cools()
    transactions = account_manager.get_transactions()
    
    return render_template('index.html', balance=f'{balance:0.2f}', cools=cools, transactions=transactions, title=os.getenv("TITLE"))

@app.route('/cool', methods=['POST'])
def cool():
    cool_type = request.form['cool_type']
    if cool_type == '0':
        cool = "Dude! Not cool!"
    elif cool_type == '2':
        cool = "Awesome! Very cool!"
    app.logger.debug(f'cool? {cool}')
    transaction = account_manager.Transaction(0, int(cool_type), cool)
    app.logger.debug('Entering not cool transaction')
    account_manager.enter_transaction(transaction)
    cools = account_manager.get_cools()

    return render_template('cool.html', cool_type=cool_type, description=cool, cools=cools, title=os.getenv("TITLE"))

@app.route('/delete', methods=['POST'])
def delete():
    date = request.form['date']
    app.logger.debug('Deleteing transaction')
    account_manager.delete_transaction(date)

    return redirect(url_for('index'))

@app.route('/enter_transaction', methods=['POST'])
def enter_transaction():
    amount = float(request.form['amount'])
    type = int(request.form['type'])
    description = request.form['description']
    transaction = account_manager.Transaction(amount, type, description)
    app.logger.debug('Entering transaction')
    account_manager.enter_transaction(transaction)

    if type == 0 or type == 2:
        return redirect(url_for('cool'))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

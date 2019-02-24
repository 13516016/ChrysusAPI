from sqlalchemy import select, update
from .payment_model import account_model, Account

class PaymentRepository:
  def __init__(self, db_conn):
    self.db_conn = db_conn

  def find_all_account(self):
    query = select([account_model])
    result_proxy = self.db_conn.execute(query)
    accounts = []
    for result in result_proxy:
      if (result):
        accounts.append(Account(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
    return accounts

  def find_account_by_firebase_uid(self, firebase_uid):
    query = select([account_model]).where(account_model.c.firebase_uid==firebase_uid)
    result_proxy = self.db_conn.execute(query)
    account = {}
    for result in result_proxy:
      if (result):
        account = Account(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
    return account

  def find_account_by_phone(self, phone):
    query = select([account_model]).where(account_model.c.phone==phone)
    result_proxy = self.db_conn.execute(query)
    account = {}
    for result in result_proxy:
      if (result):
        account = Account(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
    return account

  def increase_account_balance(self, firebase_uid, amount):
    query = update(account_model).where(account_model.c.firebase_uid==firebase_uid).values(balance=account_model.c.balance + amount)
    result_proxy = self.db_conn.execute(query)
    return result_proxy.rowcount > 0

  def decrease_account_balance(self, firebase_uid, amount):
    query = update(account_model).where(account_model.c.firebase_uid==firebase_uid).values(balance=account_model.c.balance - amount)
    result_proxy = self.db_conn.execute(query)
    return result_proxy.rowcount > 0
    
  def save_device_token(self, uid, token):
    query = update(account_model).where(account_model.c.firebase_uid==uid).values(device_token=token)
    result_proxy = self.db_conn.execute(query)
    return result_proxy.rowcount > 0
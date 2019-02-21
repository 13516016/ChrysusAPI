from sqlalchemy import select, update
from .payment_model import account_model, Account

class PaymentRepository:
  def __init__(self, db_conn):
    self.db_conn = db_conn

  def find_all_account(self):
    query = select([account_model])
    result_proxy = self.db_conn.execute(query)
    return result_proxy

  def find_account_by_firebase_uid(self, firebase_uid):
    query = select([account_model]).where(account_model.c.firebase_uid==firebase_uid)
    result_proxy = self.db_conn.execute(query)
    return result_proxy

  def increase_account_balance(self, firebase_uid, amount):
    query = update(account_model).where(account_model.c.firebase_uid==firebase_uid).values(balance=account_model.c.balance + amount)
    result_proxy = self.db_conn.execute(query)
    return result_proxy

  def decrease_account_balance(self, firebase_uid, amount):
    query = update(account_model).where(account_model.c.firebase_uid==firebase_uid).values(balance=account_model.c.balance - amount)
    result_proxy = self.db_conn.execute(query)
    return result_proxy
    

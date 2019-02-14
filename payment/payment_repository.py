from sqlalchemy import select
from .payment_model import account_model, Account

class PaymentRepository:
  def __init__(self, db_conn):
    self.db_conn = db_conn

  def find_all_account(self):
    query = select([account_model])
    result_proxy = self.db_conn.execute(query)
    return result_proxy

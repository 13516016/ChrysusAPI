from sqlalchemy import select
from .news_model import news_model, News

class NewsRepository:
  def __init__(self, db_conn):
    self.db_conn = db_conn

  def find_all_account(self):
    query = select([news_model])
    result_proxy = self.db_conn.execute(query)
    return result_proxy

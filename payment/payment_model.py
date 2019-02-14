from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

class Account:
  def __init__(self, account_id, account_no, balance):
    self.account_id = account_id
    self.account_no = account_no
    self.balance = balance

  def __eq__(self,other):
    return self.account_id == other.account_id and self.account_no == other.account_no and self.balance == other.balance

class Transaction:
  def __init__(self, transaction_id, sender_account_no, receiver_account_no,amount):
    self.transaction_id = transaction_id
    self.sender_account_no = sender_account_no
    self. receiver_account_no =  receiver_account_no
    self.amount = amount
    
  def __eq__(self,other):
    return \
      self.account_id == other.account_id and \
      self.sender_account_no == other.sender_account_no and \
      self.amount == other.amount and \
      self.amount == other.amount

account_model = Table(
  'account', metadata,
  Column('account_id', Integer, primary_key=True),
  Column('account_no', String), 
  Column('balance', Integer))

transaction_model = Table(
  'transaction', metadata, 
  Column('transaction_id', Integer, primary_key=True),
  Column('sender_account_id', None, ForeignKey('account.account_id')),
  Column('receiver_account_id', None, ForeignKey('account.account_id')),
  Column('amount', Integer)
)

def create_payment_model(engine):
  metadata.create_all(engine)
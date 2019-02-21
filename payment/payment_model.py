from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

class Account:
  def __init__(self, account_id, firebase_uid,name, address, phone, balance):
    self.account_id = account_id
    self.firebase_uid = firebase_uid
    self.balance = balance
    self.name = name
    self.address = address
    self.phone = phone

  def __eq__(self,other):
    return self.firebase_uid == other.firebase_uid and self.account_no == other.account_no and self.balance == other.balance and self.name == other.name and self.address == other.address and self.phone == other.phone

  def serialize(self):
    return self.__dict__

class Transaction:
  def __init__(self, transaction_id, sender_account_no, receiver_account_no,amount):
    self.transaction_id = transaction_id
    self.sender_account_no = sender_account_no
    self. receiver_account_no =  receiver_account_no
    self.amount = amount
    
  def __eq__(self,other):
    return \
      self.firebase_uid == other.firebase_uid and \
      self.sender_account_no == other.sender_account_no and \
      self.amount == other.amount and \
      self.amount == other.amount
  
  def serialize(self):
    return self.__dict__

account_model = Table(
  'account', metadata,
  Column('account_id', Integer, primary_key=True),
  Column('firebase_uid', String), 
  Column('name', String), 
  Column('address', String), 
  Column('phone', String), 
  Column('balance', Integer))

transaction_model = Table(
  'transaction', metadata, 
  Column('transaction_id', Integer, primary_key=True),
  Column('sender_account_uid', String),
  Column('receiver_account_uid', String),
  Column('amount', Integer)
)

def create_payment_model(engine):
  metadata.create_all(engine)
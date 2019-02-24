from .payment_model import Account

class PaymentUsecase:
  def __init__(self, repository):
    self.repository = repository 

  def get_all_account(self):
    accounts = self.repository.find_all_account()
    return accounts
    
  def get_account_by_firebase_uid(self, firebase_uid):
    account = self.repository.find_account_by_firebase_uid(firebase_uid)
    return account
 
  def get_account_by_phone(self, phone):
    account = self.repository.find_account_by_phone(phone)
    return account

  def transfer_money(self, sender_uid, receiver_phone, amount):
    sender_account = self.get_account_by_firebase_uid(sender_uid)
    if (sender_account.balance < amount):
      return False
    receiver_account = self.get_account_by_phone(receiver_phone)
    decrease_success = self.repository.decrease_account_balance(sender_uid, amount)
    if (decrease_success):
      increase_success = self.repository.increase_account_balance(receiver_account.firebase_uid, amount)
      if (increase_success):
        return True
    return False

  def register_device_token(self, uid, token):
    if (self.repository.save_device_token(uid, token)):
      return True
    return False


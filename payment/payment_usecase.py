from .payment_model import Account

class PaymentUsecase:
  def __init__(self, repository):
    self.repository = repository 

  def get_all_account(self):
    result_proxy = self.repository.find_all_account()
    accounts = []
    for result in result_proxy:
      if (result):
        accounts.append(Account(result[0],result[1],result[2]))

    return accounts
    
  def get_account_by_firebase_uid(self, firebase_uid):
    result_proxy = self.repository.find_account_by_firebase_uid(firebase_uid)
    account = {}
    for result in result_proxy:
      if (result):
        account = Account(result[0], result[1], result[2], result[3], result[4], result[5])
    return account

  def transfer_money(self, sender_uid, receiver_uid, amount):
    sender_account = self.get_account_by_firebase_uid(sender_uid)
    if (sender_account.balance < amount):
      return False

    result = self.repository.decrease_account_balance(sender_uid, amount)
    if (result.rowcount > 0):
      print(result.rowcount)
      result = self.repository.increase_account_balance(receiver_uid, amount)
      if (result.rowcount > 0):
        print(result.rowcount)
        return True
    return False


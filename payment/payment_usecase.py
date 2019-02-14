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

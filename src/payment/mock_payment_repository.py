class MockPaymentRepository:
  def __init__(self, mock_account_data):
    self.account_data = mock_account_data
  
  def find_all_account(self):
    return self.account_data

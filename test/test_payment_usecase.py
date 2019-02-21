import unittest
from src.payment.payment_usecase import PaymentUsecase
from src.payment.payment_model import Account
from src.payment.mock_payment_repository import MockPaymentRepository

mock_account_data = [
  (1,"XC1414124",2000),
  (2,"XC1423456",3000),
  (3,"XC1240192",1000)
]

class TestPaymentUsecase(unittest.TestCase):
  def test_find_all_empty(self):
    mock_payment_repository = MockPaymentRepository([()])
    payment_usecase = PaymentUsecase(mock_payment_repository)    
    expected_result = []
    self.assertEqual(payment_usecase.get_all_account(), expected_result)

  def test_find_all_filled(self):
    mock_payment_repository = MockPaymentRepository(mock_account_data)
    payment_usecase = PaymentUsecase(mock_payment_repository)
    expected_result = [Account(row[0], row[1], row[2]) for row in mock_account_data]    
    self.assertEqual(payment_usecase.get_all_account(), expected_result)

  

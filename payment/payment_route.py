from flask import Blueprint, request, jsonify
from .payment_model import Account
import json

def payment_blueprint(payment_usecase):
  blueprint = Blueprint('payment', __name__)

  @blueprint.route('/', methods=["GET"])
  def get_all_accounts():
    if request.method == "GET":
       accounts = payment_usecase.get_all_account()
       return jsonify({'success': True, 'data': [account.serialize() for account in accounts]})

  @blueprint.route('/<firebase_uid>', methods=["GET"])
  def get_account_by_uid(firebase_uid):
    if request.method == "GET":
      account = payment_usecase.get_account_by_firebase_uid(firebase_uid)
      if isinstance(account, Account):
        return jsonify({'success': True, 'data': account.serialize()})
      else:
        return jsonify({'success': False})
  
  @blueprint.route('/pay', methods=["POST"])
  def send_money():
    if request.method == "POST":
      if (not request.is_json):
        return jsonify({'success': False})

      params = request.get_json()
      sender_account_uid = params['sender_account']
      receiver_account_uid = params['receiver_account']
      amount = params['amount']
      if (payment_usecase.transfer_money(sender_account_uid, receiver_account_uid, amount)):
        return jsonify({'success': True})
      else:
        return jsonify({'success': False})

  return blueprint
from flask import Blueprint, request, jsonify


def payment_blueprint(payment_usecase):
  blueprint = Blueprint('payment', __name__)

  @blueprint.route('/', methods=["GET"])
  def get_all_accounts():
    if request.method == "GET":
       accounts = payment_usecase.get_all_account()
       return jsonify({'accounts': [account.serialize() for account in accounts]})

  return blueprint
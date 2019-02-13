from flask import Blueprint, render_template

payment = Blueprint('payment', __name__)

@payment.route('')
from flask import Blueprint, request, jsonify
import json

def news_blueprint(news_usecase):
  blueprint = Blueprint('news', __name__)

  @blueprint.route('/', methods=["GET"])
  def get_all_news():
    if request.method == "GET":
       news = news_usecase.get_all_news()
       return jsonify({'success':True, 'data': [article.serialize() for article in news]})

  return blueprint
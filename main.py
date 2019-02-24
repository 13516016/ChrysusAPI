from flask import Flask
from sqlalchemy import create_engine, select
from payment import payment_model, payment_repository, payment_usecase, payment_route
from news import news_model, news_repository, news_usecase, news_route
from firebase.firebase_service import FirebaseService
from firebase_admin import credentials, initialize_app

import configparser

def read_config(config_filename='config.ini'):
  config = configparser.ConfigParser()
  config.read(config_filename)
  return config

def create_app(usecases):
  app = Flask(__name__)
  app.register_blueprint(payment_route.payment_blueprint(usecases["payment"]), url_prefix='/payment')
  app.register_blueprint(news_route.news_blueprint(usecases["news"]), url_prefix='/news')
  return app

def connect_db(username, password, host, dbname ):
  engine = create_engine(f'postgresql://{username}:{password}@{host}/{dbname}')
  return engine

def create_models(engine):
  payment_model.create_payment_model(engine)
  news_model.create_news_model(engine)

def create_repositories(db_connection):
  repositories = {}
  repositories["payment"] = payment_repository.PaymentRepository(db_connection)
  repositories["news"] = news_repository.NewsRepository(db_connection)
  return repositories

def create_services():
  services = {}
  services["firebase"] = FirebaseService()
  return services

def create_usecases(repositories, services):
  usecases = {}
  usecases["payment"]=payment_usecase.PaymentUsecase(repositories["payment"], services["firebase"])
  usecases["news"]=news_usecase.NewsUsecase(repositories["news"])
  return usecases

def initialize_firebase():
  cred = credentials.Certificate("./firebase_cred.json")
  initialize_app(cred)

if __name__ == "__main__":
  config = read_config('config.ini')
  initialize_firebase()
  engine = connect_db(
    config["POSTGRESQL"]["Username"],
    config["POSTGRESQL"]["Password"],
    config["POSTGRESQL"]["Host"],
    config["POSTGRESQL"]["DBName"])
  create_models(engine)
  db_connection = engine.connect()
  repositories = create_repositories(db_connection)
  services = create_services()
  usecases = create_usecases(repositories, services)

  app = create_app(usecases)
  app.run(debug=False)
  
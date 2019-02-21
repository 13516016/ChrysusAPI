from flask import Flask
from sqlalchemy import create_engine, select
from payment import payment_model, payment_repository, payment_usecase, payment_route
from news import news_model, news_repository, news_usecase, news_route
import configparser

def read_config(config_filename='config.ini'):
  config = configparser.ConfigParser()
  config.read(config_filename)
  return config

def connect_db(username, password, host, dbname ):
  engine = create_engine(f'postgresql://{username}:{password}@{host}/{dbname}')
  return engine

def create_models(engine):
  payment_model.create_payment_model(engine)
  news_model.create_news_model(engine)

def create_repositories(db_connection):
  repositories = {}
  repositories["payment"] = payment_repository.PaymentRepository(db_connection)
  return repositories

def create_usecases(repositories):
  usecases = {}
  usecases["payment"]=payment_usecase.PaymentUsecase(repositories["payment"])
  return usecases

config = read_config('config.ini')
engine = connect_db(
  config["POSTGRESQL"]["Username"],
  config["POSTGRESQL"]["Password"],
  config["POSTGRESQL"]["Host"],
  config["POSTGRESQL"]["DBName"])
create_models(engine)
db_connection = engine.connect()
repositories = create_repositories(db_connection)
usecases = create_usecases(repositories)

app = Flask(__name__)
app.register_blueprint(payment_route.payment_blueprint(usecases["payment"]), url_prefix='/payment')
app.run(port=8080)

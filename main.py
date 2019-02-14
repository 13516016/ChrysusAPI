from flask import Flask
from sqlalchemy import create_engine, select
from payment import payment_model, payment_repository, payment_usecase
import configparser

def read_config(config_filename='config.ini'):
  config = configparser.ConfigParser()
  config.read(config_filename)
  return config

def create_app():
  app = Flask(__name__)
  return app

def connect_db(username, password, host, dbname ):
  engine = create_engine(f'postgresql://{username}:{password}@{host}/{dbname}')
  return engine

def create_models(engine):
  payment_model.create_payment_model(engine)

def create_repositories(db_connection):
  repositories = {}
  repositories["payment"] = payment_repository.PaymentRepository(db_connection)
  return repositories

def create_usecases(repositories):
  usecases = {}
  usecases["payment"]=payment_usecase.PaymentUsecase(repositories["payment"])
  return usecases

if __name__ == "__main__":
  config = read_config()
  engine = connect_db(
    config["POSTGRESQL"]["Username"],
    config["POSTGRESQL"]["Password"],
    config["POSTGRESQL"]["Host"],
    config["POSTGRESQL"]["DBName"])
  create_models(engine)
  db_connection = engine.connect()
  repositories = create_repositories(db_connection)
  usecases = create_usecases(repositories)

  app = create_app()
  
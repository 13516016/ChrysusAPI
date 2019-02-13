from flask import Flask
from database import DBConnection
import configparser

def read_config(config_filename='config.ini'):
  config = configparser.ConfigParser()
  config.read(config_filename)
  return config

def create_app():
  app = Flask(__name__)
  return app

if __name__ == "__main__":
  config = read_config()
  db_conn = DBConnection(
    user=config["DATABASE"]["User"],
    password=config["DATABASE"]["Password"],
    host=config["DATABASE"]["Host"],
    port=config["DATABASE"]["Port"],
    db=config["DATABASE"]["DBName"]
  )

  test_query = db_conn.query("INSERT INTO test(id,angka) VALUES(%s,%s)", 10,2)
  print(test_query)

  app = create_app()
  
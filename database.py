import psycopg2

class DBConnection:
  __conn_instance = None
  def __init__(self, host="", db="", user="", password="", port=""):
    if (DBConnection.__conn_instance is None):
      DBConnection.__conn_instance = psycopg2.connect(host=host, port=port, user=user, password=password, database=db)
  
  def query(self, query_string, *args):
    result = ()
    if (DBConnection.__conn_instance is None):
      raise Exception("DB not connected")
    
    cur = DBConnection.__conn_instance.cursor()
    cur.execute(query_string, args)
  
    try:
      result = cur.fetchall()
    except psycopg2.ProgrammingError as e:
      pass  

    DBConnection.__conn_instance.commit()
    cur.close()
    return result


  def __del__(self):
    DBConnection.__conn_instance.close()
  

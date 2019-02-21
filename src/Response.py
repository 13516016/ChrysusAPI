class Response:
  def __init__(self, success, data=None):
    self.success = success
    self.data = data

  def serialize(self):
    return self.__dict__

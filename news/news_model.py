from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

class News:
  def __init__(self, news_id, title, content, date, image_path):
    self.news_id = news_id
    self.title = title
    self.content = content
    self.date = date
    self.image_path = image_path

  def __eq__(self,other):
    return self.news_id == other.news_id and \
      self.title == other.title and \
      self.content == other.content and \
      self.date == other.date and \
      self.image_path == other.image_path

  def serialize(self):
    return self.__dict__

news_model = Table(
  'news', metadata,
  Column('news_id', Integer, primary_key=True),
  Column('title', String),
  Column('content', String),
  Column('date', String),
  Column('image_path', String))

def create_news_model(engine):
  metadata.create_all(engine)
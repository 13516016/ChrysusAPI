from .news_model import News

class NewsUsecase:
  def __init__(self, repository):
    self.repository = repository 

  def get_all_news(self):
    result_proxy = self.repository.find_all_news()
    news = []
    for result in result_proxy:
      if (result):
        news.append(News(result[0],result[1],result[2]))

    return news

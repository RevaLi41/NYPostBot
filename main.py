import pdb
from utils import Utils
from news import News
from grok import Grok


if __name__ == '__main__':
    #Init
    utils = Utils()
    news = News()
    grok = Grok()

    #get new urls
    articles = news.get_request(utils)
    urls = news.get_urls(articles)

    # send to LLM
    grok.send_to_grok('Tell me why trump sucks')
    
    # pdb.set_trace()
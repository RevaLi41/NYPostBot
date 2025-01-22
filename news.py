from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from utils import Utils
import sys
import pdb

class News:

    def get_request(self, utils: Utils) -> dict:
        #Init
        date = utils.get_date()
        load_dotenv()
        newsapi = NewsApiClient(api_key=f'{os.getenv("NEWS_API_KEY")}')

        # /v2/everything
        try:
            return newsapi.get_everything(
                qintitle = '-bus -train -subway -tram -trolley ("car crash" OR "car accident" OR "crash" OR "vehicle") AND (dead OR injured)',
                from_param = date,
                to = date,
                language = 'en',
                sort_by = 'relevancy')
        except:
            sys.exit()

    def get_urls(self, articles: dict) -> list:
        urls = []
        for i in range(len(articles['articles'])):
            urls.append(articles['articles'][i]['url'])
        return urls



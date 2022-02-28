import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('d7c232fa9d04483fab91df5c9c445326')
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SPECIFIC_SOURCE_API_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''
 
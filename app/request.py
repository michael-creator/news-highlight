import urllib.request,json
from .models import source
from config import Config

api_key = Config.NEWS_API_KEY

base_url = Config.NEWS_API_BASE_URL

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    get_news_url = (base_url).format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        result= getResult(get_news_response['sources'])
        return result 

def getResult(list):
    get_list=[]
    for newsitem in list:
        id = newsitem.get('id')
        name = newsitem.get('name')
        description = newsitem.get('description')
        url = newsitem.get('url')
        obj = source(id,name,description,url)
        get_list.append(obj)
    return get_list

def get_news_sources(news_sources):
    get_news_sources_url = (base_url).format(news_source,api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)
        result= getResult(get_news_sources_response['aritcles'])
        return result   

def process_results(news_source_results):

    news_sources_results = []
    
    for news_source_item in news_sources_results:
        id = news_source_item.get('id')
        author = news_source_item.get('author')
        title = news_source_item.get('title')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        urlToImage = news_source_item.get('urlToImage')
        publishedAt = news_source_item.get('publishedAt')
        content = news_source_item.get('content')

        news_source_object = news_Source(id,author,title,description,url,urlToImage,publishedAt,content)
        news_sources_results.append(news_source_object)

    return news_source_results


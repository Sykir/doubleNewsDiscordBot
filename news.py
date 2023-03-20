import dal
import secret
from lxml import html
import requests
import logging

def getLastNews(url):
    return dal.getNews(url)

def getNewsCount():
    news = dal.getAllNews()
    if news :
        return len(news)
    else:
        return 0

def addnews(url):
    dal.setNews(url)

def findNews():
    page = requests.get(secret.getSecret("URLCHECK"))
    tree = html.fromstring(page.content)
    
    articles = []
    #article = tree.xpath('//article')
    for article in tree.xpath('//article'):
        url = article.xpath(".//header/div/h2/a")[0].attrib["href"]
        title = article.xpath(".//header/div/h2/a/text()")[0]
        image = article.xpath("./figure/div/img")[0].attrib["src"]

        articlePage = requests.get(url)
        articleTree = html.fromstring(articlePage.content)
        content = ''.join(articleTree.xpath("/html/body/main/article/div[1]/div/p/text()"))

        if dal.getNews(url):
            logging.debug(f"news already displayed {url}")
        else:
            logging.info(f"news found ! {url}")
            addnews(url)
            articles.append({'title': title, 'url': url,'image': image, 'content': content})

    articles.reverse()
    return articles
import requests
import secret
import logging


def postToPage(article):
    url = f'https://graph.facebook.com/{secret.getSecret("FACEBOOK_PAGE_ID")}/feed\
?message={article["content"]}\
&link={article["url"]}\
&access_token={secret.getSecret("FACEBOOK_ACCESS_TOKEN")}'

    x = requests.post(url)

    if x.status_code != 200:
        logging.error(f'error when posting {article["title"]} to facebook, {x.text}')
    else:
        logging.info(f'news posted to facebook {article["title"]}')

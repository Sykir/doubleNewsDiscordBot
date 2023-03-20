import dal
import bot
import secret
import news
import requests
import logging
import time
logging.basicConfig(level=logging.INFO, filename='horizon.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dal.setup()
secret.setup()

logging.info(f"number of news processed {news.getNewsCount()}")

def wait_for_internet_connection():
    while True:
        try:
            response = requests.get(secret.getSecret("URLCHECK"))
            logging.info(f"Internet connection is OK")
            return
        except:
            logging.warning(f"Internet connection is missing, retry ...")
            time.sleep(10)
            pass

wait_for_internet_connection()
bot.run()
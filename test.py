import dal
import bot
import secret
import news
import logging
logging.basicConfig(level=logging.INFO, filename='horizon.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dal.setup()
secret.setup()

logging.info(f"number of news processed {news.getNewsCount()}")

news.findNews()
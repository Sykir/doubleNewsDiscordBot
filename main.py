import dal
import bot
import secret
import news

dal.setup()
secret.setup()

print(f"number of news processed {news.getNewsCount()}")

bot.run()
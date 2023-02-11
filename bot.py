import asyncio
import discord
import news
import secret
import logging

class horizon(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.checkingNews())

    async def on_ready(self):
        logging.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logging.info('------')

    async def checkingNews(self):
        await self.wait_until_ready()
        channel = self.get_channel(int(secret.getSecret("CHANNELID")))  # channel ID goes here
        while not self.is_closed():
            articles = news.findNews()
            for article in articles:
                title = f'> {article["title"]} \n> <{article["url"]}> \n'
                image = f'{article["image"]} \n '
                msg = f'```{article["content"]}\n\n```'
                await channel.send(title)
                await channel.send(image)
                await channel.send(msg)
                await channel.send("_ _")
            await asyncio.sleep(60)  # task runs every 60 seconds

async def checkNews():
    news.check()

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    client = horizon(intents=intents)
    client.run(secret.getSecret("TOKENBOT"))
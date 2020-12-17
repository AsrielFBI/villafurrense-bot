import discord
import os
import stickers
from PIL import Image


# Variables
stickersPath="../stickers"
client = discord.Client()



# When the bot starts
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# When a message is posted
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('+owo'):
        await message.channel.send('OwO!')

    if "yiff" in message.content:
        await message.channel.send('¿He oído yiff?')

    if message.content.startswith('+addSticker'):
        await stickers.addSticker(message)

    if message.content.startswith("-"):
        await stickers.useSticker(message)

    #TODO
    #if message.content=="+listStickers":



client.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
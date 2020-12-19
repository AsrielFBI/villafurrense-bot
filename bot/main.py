import discord
import os
import stickers
import help


# Variables
stickersPath="../stickers"
client = discord.Client()
commandActivator='fur '
stickerActivator='s'


# When the bot starts
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# When a message is posted
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content==('owo'):
        await message.channel.send('OwO!')
    if message.content==('uwu'):
        await message.channel.send('UwU!')

    if "yiff" in message.content:
        await message.channel.send('¿He oído yiff?')

    if message.content.startswith(commandActivator+'add'):
        await stickers.addSticker(message)

    if message.content.startswith(stickerActivator):
        await stickers.useSticker(message)

    if message.content==commandActivator+'list':
        await stickers.listStickers(message)
    if message.content==commandActivator+'help':
        await help.getHelp(message)

    if message.content==commandActivator+'aputo':
        output="Asriel puto"
        await message.channel.send(output)





    #TODO
    #if message.content=="+listStickers":



client.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
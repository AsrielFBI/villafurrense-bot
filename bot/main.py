from bot.stickers import useSticker
import discord
import os
import stickers
import help
import random


# Variables
stickersPath="../stickers"
bot = discord.Client()
commandActivator='fur '
stickerActivator='s'
n=0

# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# When a message is posted
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower()==('owo'):
        await message.channel.send('OwO!')
    if message.content.lower()==('uwu'):
        await message.channel.send('UwU!')
    if message.content.lower()==('7w7'):
        await message.channel.send(':eyes:')
    if message.content.lower()==('ewe'):
        await message.channel.send('EwE!')
    

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

    if message.content.startswith(commandActivator+'del'):
        await stickers.deleteSticker(message)

    ## FIXME
    if bot.user.id != message.author.id:
        if message.content.startswith(stickerActivator):
            # do something here, change to whatever you want
            await bot.send_message(message.channel, stickers.useSticker(message))

    if message.content.startswith(commandActivator+'guess'):
        n = random.randint(0,10)
        await message.channel.send('Adivina el numero entre 0 y 10 con guess <num>')
    if message.content.startswith('guess'):
        input=int(message.content.split()[-1])
        if input==n:
            await message.channel.send('Has acertado')
        else:
            await message.channel.send('Has fallado')
                
                






bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
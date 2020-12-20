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

# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# When a message is posted
@bot.event
async def on_message(message):

    n=0
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
            await message.channel.send(message.channel, stickers.useSticker(message))

    if message.content.startswith('guess'):
        await message.channel.send('Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await bot.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await message.channel.send(fmt.format(answer))
            return
        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('Sorry. It is actually {}.'.format(answer))

                






bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
import discord
import os
import stickers
import help
import random
import memes
from discord.ext import commands


# Variables
stickersPath="../stickers"
bot = commands.Bot(command_prefix='fur ')
commandActivator='fur '
stickerActivator='s'
statusVar=discord.Status.do_not_disturb


@bot.command(name='version')
async def version(context):
    await context.message.channel.send("hola que ase")

@bot.command(name='s')
async def s(context):
    await stickers.useSticker(context)


@bot.command(name='aputo')
async def aputo(context):
    await context.channel.send("Asriel puto")
    



# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=statusVar,activity=discord.Game('Minecraft'))


def changeStatus(input : str):
    if str=='online':
        statusVar=discord.Status.online
    if str=='offline':
        statusVar=discord.Status.offline
    if str=='do_not_disturb':
        statusVar=discord.Status.do_not_disturb

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

    #if message.content.startswith(stickerActivator):
    #    await stickers.useSticker(message)

    if message.content==commandActivator+'list':
        await stickers.listStickers(message)

    if message.content==commandActivator+'help':
        await help.getHelp(message)

    #if message.content==commandActivator+'aputo':
    #    output="Asriel puto"
    #    await message.channel.send(output)
    if message.content==commandActivator+'cputo':
        output="Cracker puto"
        await message.channel.send(output)

    if message.content.startswith(commandActivator+'del'):
        await stickers.deleteSticker(message)

    if message.content.startswith(commandActivator+'trauma'):
        await memes.trauma(message)
    if message.content.startswith(commandActivator+'horny'):
        await memes.horny(message)
    if message.content.startswith(commandActivator+'patada'):
        await memes.patada(message)
    if message.content.startswith(commandActivator+'cringe'):
        await memes.cringe(message)

    if message.content.startswith(commandActivator+'random'):
        max=message.content.split()[-1]
        output=random.randint(0, max)
        await message.channel.send(str(output))

    ## FIXME
    if bot.user.id != message.author.id:
        if message.content.startswith(stickerActivator):
            # do something here, change to whatever you want
            await message.channel.send(message.channel, stickers.useSticker(message))

    if message.content.startswith(commandActivator+'status'):
        changeStatus(message.content.split()[-1])

    await bot.process_commands(message)






bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')


import discord
import os

from discord.message import Message

import stickers
from discord.ext import commands
from PIL import Image



# Variables
stickersPath="../stickers"
bot = commands.Bot(command_prefix='fur ')
bot.remove_command('trauma')


commandActivator='fur '
stickerActivator='s '
statusVar=discord.Status.do_not_disturb

#helptxt='/app/bot/help.txt'
helptxt='help.txt'
#stickersPath='/app/stickers/'
stickersPath='../stickers/'



# Commands
@bot.command(name='version')
async def version(context):
    embed=discord.Embed(title="FurBot", description='El mejor bot furro')
    embed.add_field(name='Version', value='V 0.2',inline=False)
    await context.message.channel.send(embed=embed)



@bot.command(name='info')
async def help(context):
    """Muestra la info de Zaffy
    """
    f = open(helptxt, 'r')
    general=f.read()
    await context.channel.send(general)
    f.close()


@bot.command(name='reply')
async def reply(context ):
    print(context.message_reference)



# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=statusVar,activity=discord.Game('Cosas Furries'))


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
    if message.content.lower()==('awa'):
        await message.channel.send('AwA!')

    if message.type==0:
        await message.channel.send('dfsdafsdfaf!')


    if message.content=='mantenimiento':
        game = discord.Game("En manetenimiento")
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)


    if message.content.startswith('!hello'):
        print(message.reference)
        await message.reply('Hello!', mention_author=True)

    

    

    if "yiff" in message.content:
        await message.channel.send('¿He oído yiff?')

    if message.content.startswith(commandActivator+'add'):
        await stickers.addSticker(message)

    if message.content.startswith(stickerActivator):
        await stickers.useSticker(message)

    if message.content==commandActivator+'list':
        await stickers.listStickers(message)

    if message.content.startswith(commandActivator+'del'):
        await stickers.deleteSticker(message)


    await bot.process_commands(message)


extensions=['roast', 'memes', 'fun']
for extension in extensions:
    bot.load_extension(extension)

bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')


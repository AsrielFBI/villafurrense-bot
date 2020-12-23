import discord
import os

from discord.message import Message

import stickers
from discord.ext import commands
from PIL import Image



# Variables
stickersPath="../stickers"
bot = commands.Bot(command_prefix='fur ', owner_id = 315111397837111296)
bot.remove_command('trauma')

if os.path.isfile('~/villafurrense-bot/bot/help.txt') :
    helptxt='~/villafurrense-bot/bot/help.txt'
else:
    helptxt='/app/bot/help.txt'

#helptxt='/app/bot/help.txt'
#helptxt='help.txt'
#stickersPath='/app/stickers/'
#stickersPath='../stickers/'



# Commands
@bot.command(name='version')
async def version(context):
    embed=discord.Embed(title="FurBot", description='El mejor bot furro')
    embed.add_field(name='Version', value='V 0.2',inline=False)
    print(os.path.exists('../stickers/'))
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
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game('En mantenimiento'))


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
    if "yiff" in message.content:
        await message.channel.send('¿He oído yiff?')

    if message.content=='mantenimiento':
        game = discord.Game("En manetenimiento")
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)

    if message.content.startswith('!hello'):
        print(message.reference)
        await message.reply('Hello!', mention_author=True)

    await bot.process_commands(message)

# Add extensions
extensions=['roast', 'memes', 'fun', 'animal', 'stickers', 'utilities']
for extension in extensions:
    bot.load_extension(extension)

bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
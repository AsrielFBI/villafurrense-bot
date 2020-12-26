import discord
import os
from discord import channel
from discord import activity
from discord.message import Message
import stickers
from discord.ext import commands
from PIL import Image
from dotenv import load_dotenv

# Change where is the token
load_dotenv()
if os.path.isdir('../memes/') :
    token= os.getenv('DISCORD_TOKEN')
else:
    token=os.environ.get('DISCORD_TOKEN', None)


# Change discord game and activity depending if it's running in server
if os.path.isdir('../memes/') :
    status=discord.Status.do_not_disturb
    activity=discord.Game('En mantenimiento')
else:
    status=discord.Status.online
    activity=discord.Game('Cosas furries')


bot = commands.Bot(command_prefix='fur ', owner_id = 315111397837111296)
bot.remove_command('trauma')


@bot.command(name='reply')
async def reply(context ):
    print(context.message_reference)



# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=status,activity=activity)


# When a message is posted
@bot.event
async def on_message(message):

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

    if message.content.startswith('!hello'):
        print(message.reference)
        await message.reply('Hello!', mention_author=True)

    await bot.process_commands(message)

# Add extensions
extensions=['roast', 'memes', 'fun', 'animal', 'stickers', 'utilities', 'administration', 'music']
for extension in extensions:
    bot.load_extension(extension)


bot.run(token)
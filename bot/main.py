import discord
import os
import stickers
import random
import memes
from discord.ext import commands
from PIL import Image



# Variables
stickersPath="../stickers"
bot = commands.Bot(command_prefix='fur ')
bot.remove_command('trauma')

statusVar=discord.Status.online

#helptxt='/app/bot/help.txt'
helptxt='help.txt'
#stickersPath='/app/stickers/'
stickersPath='../stickers/'



# Commands
@bot.command(name='version')
async def version(context):
    embed=discord.Embed(title="Version", description='Version 0.2')
    embed.add_field(name='Version', value='V0.2',inline=False)
    await context.message.channel.send(embed=embed)



@bot.command(name='info')
async def help(context):
    f = open(helptxt, 'r')
    general=f.read()
    await context.channel.send(general)
    f.close()



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


extensions=['roast', 'memes']
for extension in extensions:
    bot.load_extension(extension)

bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')


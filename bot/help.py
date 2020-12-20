import discord
import os

client = discord.Client()

if os.path.isfile('~/proyectos/villafurrense-bot/bot'):
    txt='~/proyectos/villafurrense-bot/bot/help.txt'
else:
    txt='/app/bot/help.txt'

@client.event
async def getHelp(message):
    f = open(txt, 'r')
    general=f.read()
    await message.channel.send(general)
    f.close()


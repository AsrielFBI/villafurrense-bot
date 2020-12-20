import discord
import os

client = discord.Client()


@client.event
async def getHelp(message):
    f = open('help.txt', 'r')
    general=f.read()
    await message.channel.send(general)
    f.close()


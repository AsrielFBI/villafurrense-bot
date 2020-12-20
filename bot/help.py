import discord
import os

client = discord.Client()

# Files
f = open('example.txt', 'r')
general=f.read()




@client.event
async def getHelp(message, general):
    
    await message.channel.send(general)


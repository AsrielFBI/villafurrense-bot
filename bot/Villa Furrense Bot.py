import discord
import os

client = discord.Client()

# When the bot stats
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# When a message is posted
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
from bot.stickers import useSticker
import discord
import os
import stickers
import help


# Variables
stickersPath="../stickers"
bot = discord.bot()
commandActivator='fur '
stickerActivator='s'


# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# When a message is posted
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content==('owo'):
        await message.channel.send('OwO!')
    if message.content==('uwu'):
        await message.channel.send('UwU!')
    if message.content==('7w7'):
        await message.channel.send(':eyes:')

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

    if bot.user.id != message.author.id:
        if message.content.startswith(stickerActivator):
            # do something here, change to whatever you want
            await bot.send_message(message.channel, stickers.useSticker(message))
        await bot.process_commands(message)



bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')
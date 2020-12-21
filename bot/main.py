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



commandActivator='fur '
stickerActivator='s '
statusVar=discord.Status.online



helptxt='/app/bot/help.txt'
#helptxt='help.txt'
memePath='/app/memes/'
#memePath='../memes/'
stickersPath='/app/stickers/'
#stickersPath='../stickers/'



# Commands
@bot.command(name='version')
async def version(context):
    embed=discord.Embed(title="Version", description='Version 0.2')
    embed.add_field(name='Version', value='V0.2',inline=False)
    await context.message.channel.send(embed)

@bot.command(name='aputo')
async def aputo(context):
    await context.channel.send("Asriel puto")

@bot.command(name='cputo')
async def cputo(context):
    await context.channel.send("Cracker puto")

@bot.command(name='tputo')
async def cputo(context):
    await context.channel.send("Thedax puto")

@bot.command(name='info')
async def help(context):
    f = open(helptxt, 'r')
    general=f.read()
    await context.channel.send(general)
    f.close()

    
################### Memes ##########################

class memes(commands.Cog):
    @commands.command()
    async def trauma(context, user : discord.Member=None):
        
        """Creates a trauma meme with the user photo

        Args:
            message ([type]): [description]
        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",670)

        # Open images
        background = Image.open(memePath+"trauma.png").convert("RGBA")
        width, height = background.size
        output=Image.new("RGBA",(width,height))
        img = Image.open(memePath+"01.png").convert("RGBA")
        output.paste(img, (39,400), img)
        output.paste(background, (0,0), background)
        output.save(memePath+"output.png","PNG")

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    @commands.command()
    async def horny(context, user : discord.Member=None):
        """Creates a horny meme with the user photo

        Args:
            message ([type]): [description]
        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",300)

        # Open images
        background = Image.open(memePath+"horny.png").convert("RGBA")
        width, height = background.size
        output=Image.new("RGBA",(width,height))
        img = Image.open(memePath+"01.png").convert("RGBA")
        output.paste(img, (410,180), img)
        output.paste(background, (0,0), background)
        output.save(memePath+"output.png","PNG")

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")

    @commands.command()
    async def patada(context, user : discord.Member=None):
        """Creates a patada meme with the user photo

        Args:
            message ([type]): [description]
        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",110)

        # Open images
        background = Image.open(memePath+"patada.png").convert("RGBA")
        width, height = background.size
        output=Image.new("RGBA",(width,height))
        img = Image.open(memePath+"01.png").convert("RGBA")
        output.paste(img, (198,229), img)
        output.paste(img, (348,917), img)
        output.paste(background, (0,0), background)
        output.save(memePath+"output.png","PNG")

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    @commands.command()
    async def cringe(context, user : discord.Member=None):
        """Creates a patada meme with the user photo

        Args:
            message ([type]): [description]
        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",170)

        # Open images
        background = Image.open(memePath+"cringe.png").convert("RGBA")
        width, height = background.size
        output=Image.new("RGBA",(width,height))
        img = Image.open(memePath+"01.png").convert("RGBA")
        output.paste(img, (370,20), img)
        output.paste(background, (0,0), background)
        output.save(memePath+"output.png","PNG")

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    def convertPic(picture, imgName, imgSize):
        img = Image.open(picture)

        wpercent = (imgSize/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((imgSize,hsize), Image.ANTIALIAS)

        img.save(memePath+imgName+'.png')



################ Stickers ###################



# When the bot starts
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=statusVar,activity=discord.Game('Cosas Furries'))


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

    if message.content.startswith(stickerActivator):
        await stickers.useSticker(message)

    if message.content==commandActivator+'list':
        await stickers.listStickers(message)

    if message.content.startswith(commandActivator+'del'):
        await stickers.deleteSticker(message)

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





bot.add_cog(memes())
bot.run('Nzg4NDc3MDcyOTU1NjcwNTI4.X9kEfw.yg5Q_RitwWG7K0dTlQPs4-umziQ')


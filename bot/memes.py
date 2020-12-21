import discord
from discord.ext import commands
from PIL import Image
import os




memePath='/app/memes/'
#memePath='../memes/'
class memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    def convertPic(picture, imgName, imgSize):
        img = Image.open(picture)

        wpercent = (imgSize/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((imgSize,hsize), Image.ANTIALIAS)

        img.save(memePath+imgName+'.png')


    @commands.command()
    async def trauma(self, context, *, user : discord.Member=None):
        
        """Uso: fur trauma <@user>

        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        memes.convertPic(memePath+"01.webp","01",670)

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
    async def horny(self, context, *, user : discord.Member=None):
        """Uso: fur horny <@user>

        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        memes.convertPic(memePath+"01.webp","01",300)

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
    async def patada(self, context, *, user : discord.Member=None):
        """Uso: fur patada <@user>

        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        memes.convertPic(memePath+"01.webp","01",110)

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
    async def cringe(self, context, *, user : discord.Member=None):
        """Creates a patada meme with the user photo

        """

        # Get user avatar
        avatarUrl=user.avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        memes.convertPic(memePath+"01.webp","01",170)

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

def setup(bot):
    bot.add_cog(memes(bot))

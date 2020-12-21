import discord
from discord.ext import commands
from PIL import Image
import os



#stickersPath='/app/stickers/'
stickersPath='../stickers/'
stickerSize=500


class memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    @commands.command()
    async def addSticker(self, context, *, user : discord.Member=None):
        """Añade un sticker para usarlo con el bot"""
        stickerName=context.content.split()[-1]
        print(stickerName)
        stickerExtension=context.content.split(".")[-1]
        if memes.checkSticker(stickerName, stickerExtension)==0:
            await context.channel.send("El nombre de sticker ya existe")
            return
        if memes.checkSticker(stickerName, stickerExtension)==1:
            await context.channel.send("El tipo de archivo no es válido")
            return
        
        if stickerExtension=='jpg':
            stickerFileName=stickerName+".jpg"
        else:
            stickerFileName=stickerName+".png"

        stickerUrl=context.attachments[0].url
        var="wget -O %s%s %s"%(stickersPath, stickerFileName, stickerUrl)
        stickerPath="%s%s"%(stickersPath ,stickerFileName)
        os.system(var)
        memes.convertPic(stickerPath, stickerName)

    def checkSticker(stickerName, stickerExtension):
        """[summary]

        Args:
            stickerName ([String]): [description]
            stickerExtension ([String]): [description]

        Returns:
            [0]: [name used by other sticker]
            [1]: [if file extension is correct]
        """
        str=os.listdir(stickersPath)
        str[:] = [s.replace('.png', '') for s in str]
        str[:] = [s.replace("'", '') for s in str]
        if stickerName in str:
            return 0
        if stickerExtension in ['jpg', 'png']:
            return 1

    @commands.command
    async def useSticker(self, context, *, user : discord.Member=None):
        stickerName=stickersPath
        stickerName+=context.content[context.content.find(" ")+1:].split()[0]
        stickerName+=".png"
        await context.channel.send(file=discord.File(stickerName))



    # Resize and image and save it as png
    def convertPic(picture, stickerName):
        img = Image.open(picture)

        wpercent = (stickerSize/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((stickerSize,hsize), Image.ANTIALIAS)

        img.save(stickersPath+stickerName+'.png')
        

    @commands.command
    async def listStickers(self, context, *, user : discord.Member=None):
        str=os.listdir(stickersPath)

        str[:] = [s.replace('.png', '') for s in str]
        str[:] = [s.replace("'", '') for s in str]
        await context.channel.send(str)

    @commands.command
    async def deleteSticker(self, context, *, user : discord.Member=None):
        stickerName=context.content.split()[-1]
        str='rm '+stickersPath+stickerName
        os.system(str)
        await context.channel.send(stickerName+' eliminado')

    



   
def setup(bot):
    bot.add_cog(memes(bot))

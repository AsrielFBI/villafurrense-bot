import discord
from discord.ext import commands
import os
from PIL import Image
from discord.ext.commands.core import command


if os.path.isdir('../stickers/') :
    stickersPath='../stickers/'
else:
    stickersPath='/app/stickers/'

stickerSize=500


class stickers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, context,arg1):
        """ Añade un sticker 

             Uso: seleccionar una imagen y en el cuadro de "añadir comentario"
             poner fur add <nombre_sticker>
        """

        # Checks if a picture is correct
        stickerExtension=context.message.attachments[0].url.split(".")[-1]
        if checkSticker(arg1, stickerExtension)==0:
            await context.channel.send("El nombre de sticker ya existe")
            return
        
        if stickerExtension=='jpg':
            stickerFileName=arg1+".jpg"
        else:
            stickerFileName=arg1+".png"

        stickerUrl=context.message.attachments[0].url
        var="wget -O %s%s %s"%(stickersPath, stickerFileName, stickerUrl)
        stickerPath="%s%s"%(stickersPath ,stickerFileName)
        os.system(var)
        convertPic(stickerPath, arg1)

        
        if stickerExtension=='jpg':
            var2="rm "+stickerPath
            os.system(var2)
        await context.channel.send("Sticker "+arg1+" añadido")


    @commands.command()
    async def list(self, context):
        """ Nombre de los stickers añadidos

        """
        str=os.listdir(stickersPath)

        str[:] = [s.replace('.png', '') for s in str]
        str[:] = [s.replace("'", '') for s in str]
        await context.channel.send(str)


    @commands.command(name='s')
    async def useSticker(self, context,sticker):
        """ Usar un sticker

            Uso: fur s <nombre_sticker>
        """
        stickerName=stickersPath
        stickerName+=sticker
        stickerName+=".png"
        await context.channel.send(file=discord.File(stickerName))



# Resize and image and save it as png
def convertPic(picture : str, stickerName : str):
    """Converts a picture to a sticker

    Args:
        picture (str): [picture to convert]
        stickerName (str): [name of the sticker to be created]
    """

    img = Image.open(picture)
    wpercent = (stickerSize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((stickerSize,hsize), Image.ANTIALIAS)
    img.save(stickersPath+stickerName+'.png')



def checkSticker(stickerName : str, stickerExtension : str):
    """ checks if a sticker already exists and if file extension is correct

    Args:
        stickerName ([String]): [Name of sticker to add]
        stickerExtension ([String]): [Extension of sticker to add]

    Returns:
        [0]: [name used by other sticker]
        [1]: [if file extension is correct, must be jpg or png]
    """
    str=os.listdir(stickersPath)
    str[:] = [s.replace('.png', '') for s in str]
    str[:] = [s.replace("'", '') for s in str]
    if stickerName in str:
        return 0
    if stickerExtension in ['jpg', 'png']:
        return 1



def setup(bot):
    bot.add_cog(stickers(bot))

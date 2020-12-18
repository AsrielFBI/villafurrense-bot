from math import isnan
import discord
import os
from PIL import Image

# Variables
client = discord.Client()
stickersPath='../stickers/'
stickerSize=500


 
@client.event
async def addSticker(message):
    """ Downloads a sticker and converts it to png if it is other format

    Args:
        message: contains the sticker to add
    """
    stickerName=message.content[message.content.find(" ")+1:]
    stickerExtension=message.content.split(".")[-1]
    if stickerExtension=='jpg':
        stickerFileName=stickerName+".jpg"
    else:
        stickerFileName=stickerName+".png"
    stickerUrl=message.attachments[0].url
    var="wget -O ../stickers/%s %s"%(stickerFileName, stickerUrl)
    stickerPath="../stickers/%s"%(stickerFileName)
    os.system(var)
    convertPic(stickerPath, stickerName)

    
    if stickerExtension=='jpg':
        var2="rm "+stickerPath
        os.system(var2)
    await message.channel.send("Sticker "+stickerName+" añadido")



@client.event
async def useSticker(message):
    stickerName="../stickers/"
    stickerName+=message.content[message.content.find("_")+1:].split()[0]
    stickerName+=".png"
    await message.channel.send(file=discord.File(stickerName))



# Resize and image and save it as png
def convertPic(picture, stickerName):
    img = Image.open(picture)

    wpercent = (stickerSize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((stickerSize,hsize), Image.ANTIALIAS)

    img.save(stickersPath+stickerName+'.png')
    

@client.event
async def listStickers(message):
    str=os.listdir(stickersPath)

    str[:] = [s.replace('.png', '') for s in str]
    str[:] = [s.replace("'", '') for s in str]
    await message.channel.send(str)


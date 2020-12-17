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
    stickerName=message.content[message.content.find(" ")+1:]
    print(stickerName)
    stickerFileName=stickerName+".jpeg"
    print(stickerName)
    stickerUrl=message.attachments[0].url
    print(stickerUrl)
    var="wget -O ../stickers/%s %s"%(stickerFileName,stickerUrl)
    stickerPath="../stickers/%s"%(stickerFileName)
    print(var)
    os.system(var)
    convertPic(stickerPath, stickerName)
    
    var2="rm "+stickerPath
    os.system(var2)
    await message.channel.send("Sticker "+stickerName+" añadido")



@client.event
async def useSticker(message):
    stickerName="../stickers/"
    stickerName+=message.content[message.content.find("-")+1:].split()[0]
    stickerName+=".png"
    await message.channel.send(file=discord.File(stickerName))
#def listStickers():



# Resize and image and save it as png
def convertPic(picture, stickerName):
    img = Image.open(picture)

    wpercent = (stickerSize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((stickerSize,hsize), Image.ANTIALIAS)

    img.save(stickersPath+stickerName+'.png')
    
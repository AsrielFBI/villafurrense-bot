from math import isnan
import discord
import os

client = discord.Client()


def addSticker(message):
    stickerName=message.content[message.content.find(" ")+1:]
    print(stickerName)
    stickerName+=".jpeg"
    print(stickerName)
    stickerUrl=message.attachments[0].url
    print(stickerUrl)
    var="wget -O ../stickers/%s %s"%(stickerName,stickerUrl)
    stickerPath="../stickers/%s"%(stickerName)
    print(var)
    os.system(var)
    saveSticker(stickerPath)


#def useSticker(stickerName, message):
#def listStickers():
    
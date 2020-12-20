import discord
from PIL import Image
import os

client = discord.Client()
if os.path.isfile('../memes/'):
    memePath='../memes/'
else:
    memePath='/app/memes/'

@client.event
async def trauma(message):
    """Creates a trauma meme with the user photo

    Args:
        message ([type]): [description]
    """

    # Get user avatar
    avatarUrl=message.mentions[0].avatar_url
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
    await message.channel.send(file=discord.File(memePath+"output.png"))

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
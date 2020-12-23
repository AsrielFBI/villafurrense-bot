from asyncio.tasks import sleep
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import os


if os.path.isdir('../memes/') :
    memePath='../memes/'
else:
    memePath='/app/memes/'


    
class memes(commands.Cog):
    """Memés """
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def trauma(self, context, *, user : discord.Member=None):
        
        """Oh no traumita

            Uso: fur trauma "@<usuario>
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        # Create meme
        createMeme(('trauma','01'),avatarUrl,670,(0,0,39,400),True)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))


    @commands.command()
    async def horny(self, context, *, user : discord.Member=None):
        """Mucho horny

            Uso: fur horny "@<usuario>
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url
        
        # Create meme
        createMeme(('horny','01'),avatarUrl,300,(0,0,410,180),True)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))



    @commands.command()
    async def patada(self, context, *, user : discord.Member=None):
        """Te vas a comer mi pie
            
            Uso: fur patada "@<usuario>
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url
        
        # Create meme
        createMeme(("patada","01","01"),avatarUrl,110,(0,0,198,229,348,915),True)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))



    @commands.command()
    async def cringe(self, context, *, user : discord.Member=None):
        """That's cringy as fuck
            
            Uso: fur cringe "@<usuario>
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        # Create meme
        createMeme(('cringe','01'),avatarUrl,170,(0,0,370,20),True)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))
        


    @commands.command()
    async def españa(self, context, *, user : discord.Member=None):
        """Arriba España!!!
            
            Uso: fur españa "@<usuario>
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        # Create meme
        createMeme(("españa",'01'),avatarUrl,650,(0,0,0,0),False)

        # Create video
        var='ffmpeg -loop 1 -i {}output.png -i {}españa.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png','output.mp4'))
        


    @commands.command()
    async def burn(self, context, *, user : discord.Member=None):
        """Quema a tus amigos :)
            
            Uso: fur burn "@<usuario>  ---> quema a un amigo
                 fur burn              ---> quémate tu solo
        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        #createMeme('01', '01','burn',avatar_url=avatarUrl, avatar_size=300, position=(0,0,0,0))
        createMeme(('burn','01'),avatarUrl,300,(0,0,0,0),False)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))
        


    @commands.command()
    async def betis(self, context, *, user : discord.Member=None):
        """Olé mi Betis

        """

        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        # Create meme
        createMeme(("betis",'01'),avatarUrl,400,(-100,0,0,0),False)

        # Create video
        var='ffmpeg -loop 1 -i {}output.png -i {}betis.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp', 'output.png', '01.png','output.mp4'))
        



    #@commands.command()
    #async def smash(self, context, *, user : discord.Member=None):
    #    avatarUrl=getUser(context,user).avatar_url
    #    var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
    #    os.system(var)
#
    #    output= Image.open(memePath+'smash'+'.png').convert("RGBA")
#
    #    # Text
    #    txtImage = Image.new("L", (100, 100), 255)
    #    title_font = ImageFont.truetype(memePath+'smash.ttf', 35)
    #    text = "Yiffs into the figth"
    #    name=str(getUser(context,user))[:-5]  # remove #1234
    #    image_editable = ImageDraw.Draw(txtImage)
    #    image_editable.text((460,132), text, (237, 230, 211), font=title_font)
    #    image_editable.text((460,102), name, (237, 230, 211), font=title_font)
#
    #    #img=Image.open(memePath+'01.png').convert("RGBA")
#
    #    output.save(memePath+"output.png","PNG")
    #    await context.channel.send(file=discord.File(memePath+"output.png"))





def createMeme(pictures : list, avatar_url : str, avatar_size : int, position : list, invert : bool):
    """ Crea un meme

    Args:
        pictures (list): [lista de imagenes, siendo pictures[0] el meme y el resto avatares]
        avatar_url (str): [url del avatar a añadir al meme]
        avatar_size (int): [tamañao al que convertir el avatar de webp a png]
        position (list): [posiciones en las que colocar las imagenes, siendo position[0] y position[1] la x,y del meme]
        invert (bool): [Si es True usa el meme como canvas, en caso contrario, usa el avatar]
    """

    var="wget -O %s%s %s"%(memePath, "01.webp", avatar_url)
    os.system(var)

    # Convert avatar
    convertPic(memePath+"01.webp","01",avatar_size)


    if invert==False: # burn
        canvas=pictures[1]
        width, height = Image.open(memePath+canvas+'.png').convert("RGBA").size
    else:             # cringe
        canvas=pictures[0]
        width, height = Image.open(memePath+canvas+'.png').convert("RGBA").size
        
    output=Image.new("RGBA",(width,height))                         # Create picture
    meme=Image.open(memePath+pictures[0]+'.png').convert("RGBA")    # Open meme picture


    # Add avatar pictures
    i=2
    for x in pictures[1:]:
        img = Image.open(memePath+x+'.png').convert("RGBA")
        output.paste(img, (position[i], position[i+1]),img)
        i+=2

    # Add meme picture
    output.paste(meme,(position[0], position[1]), meme)

    # Save final meme
    output.save(memePath+"output.png","PNG")



def convertPic(picture : str, imgName : str, imgSize : str):
    """Converts an image to PNG with a differents size

    Args:
        picture (str): picture to convert
        imgName (str): exported picture name
        imgSize (str): exported image size
    """
    img = Image.open(picture)

    wpercent = (imgSize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((imgSize,hsize), Image.ANTIALIAS)

    img.save(memePath+imgName+'.png')


def getUser(context, user : discord.Member=None):
    """Gets user from a message

    Args:
        context ([Message]): [Message to get an avatar]
        user (discord.Member, optional): [User of a message]. Defaults to None.

    Returns:
        [str]: [user]
    """
    if user==None:
            avatarUrl=context.author
    else:
            avatarUrl=user

    return avatarUrl
    

def deleteRequirements(elements : list):
    """ Delete files needed to create a meme

    Args:
        elements (list): [files used in a meme]
    """
    for x in elements:
        os.system("rm "+memePath+x)


def setup(bot):
    bot.add_cog(memes(bot))

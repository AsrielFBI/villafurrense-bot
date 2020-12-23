from asyncio.tasks import sleep
import discord
from discord.ext import commands
from PIL import Image
import os
import ffmpeg




memePath='../memes/'

#memePath='/app/memes/'

    
class memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @commands.command()
    async def trauma(self, context, *, user : discord.Member=None):
        
        """Oh no traumita

            Uso: fur trauma "@<usuario>
        """
        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)


        #createMeme('01','trauma','trauma',avatarUrl,670,(39,400,0,0))
        createMeme(('trauma','01'),avatarUrl,670,(0,0,39,400),True)



        #var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        #os.system(var)
        #memes.convertPic(memePath+"01.webp","01",670)
#
        ## Open images
        #background = Image.open(memePath+"trauma.png").convert("RGBA")
        #width, height = background.size
        #output=Image.new("RGBA",(width,height))
        #img = Image.open(memePath+"01.png").convert("RGBA")
        #output.paste(img, (39,400), img)
        #output.paste(background, (0,0), background)
        #output.save(memePath+"output.png","PNG")
#
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    @commands.command()
    async def horny(self, context, *, user : discord.Member=None):
        """Mucho horny

            Uso: fur horny "@<usuario>
        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)
        


        createMeme(('horny','01'),avatarUrl,300,(0,0,410,180),True)


        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")

    @commands.command()
    async def patada(self, context, *, user : discord.Member=None):
        """Te vas a comer mi pie
            
            Uso: fur patada "@<usuario>
        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)
        

        createMeme(("patada","01","01"),avatarUrl,110,(0,0,198,229,348,915),True)

        #var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        #os.system(var)
        #memes.convertPic(memePath+"01.webp","01",110)
#
        ## Open images
        #background = Image.open(memePath+"patada.png").convert("RGBA")
        #width, height = background.size
        #output=Image.new("RGBA",(width,height))
        #img = Image.open(memePath+"01.png").convert("RGBA")
        #output.paste(img, (198,229), img)
        #img.thumbnail((90, 90), Image.ANTIALIAS)
        #output.paste(img, (348,915), img)
        #output.paste(background, (0,0), background)
        #output.save(memePath+"output.png","PNG")

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    @commands.command()
    async def cringe(self, context, *, user : discord.Member=None):
        """That's cringy as fuck
            
            Uso: fur cringe "@<usuario>
        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)

        
        createMeme(('cringe','01'),avatarUrl,170,(0,0,370,20),True)


        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")


    @commands.command()
    async def españa(self, context, *, user : discord.Member=None):
        """Arriba España!!!
            
            Uso: fur españa "@<usuario>
        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)


        createMeme(("españa",'01'),avatarUrl,650,(0,0,0,0),False)

        # Create video
        var='ffmpeg -loop 1 -i {}output.png -i {}españa.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        #await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")
        os.system("rm "+memePath+"output.mp4")



    @commands.command()
    async def burn(self, context, *, user : discord.Member=None):
        """Quema a tus amigos :)
            
            Uso: fur burn "@<usuario>  ---> quema a un amigo
                 fur burn              ---> quémate tu solo
        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)

        #createMeme('01', '01','burn',avatar_url=avatarUrl, avatar_size=300, position=(0,0,0,0))
        createMeme(('burn','01'),avatarUrl,300,(0,0,0,0),False)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")



    @commands.command()
    async def betis(self, context, *, user : discord.Member=None):
        """Olé mi Betis

        """

        # Get user avatar
        avatarUrl=getAvatarUrl(user,context)


        createMeme(("betis",'01'),avatarUrl,400,(-100,0,0,0),False)

        # Create video
        var='ffmpeg -loop 1 -i {}output.png -i {}betis.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        #await sleep(1)
        os.system("rm "+memePath+"01.webp")
        os.system("rm "+memePath+"output.png")
        os.system("rm "+memePath+"01.png")
        os.system("rm "+memePath+"output.mp4")





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



def convertPic(picture, imgName, imgSize):
    img = Image.open(picture)

    wpercent = (imgSize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((imgSize,hsize), Image.ANTIALIAS)

    img.save(memePath+imgName+'.png')



def getAvatarUrl(user, context):
    """
    docstring
    """
    if user==None:
            avatarUrl=context.author.avatar_url
    else:
            avatarUrl=user.avatar_url

    return avatarUrl
    


def setup(bot):
    bot.add_cog(memes(bot))

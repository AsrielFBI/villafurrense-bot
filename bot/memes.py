from asyncio.tasks import sleep
from operator import pos
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os
from sympy import symbols, solve
import emoji
import moviepy.editor as mp
import math


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
        await context.channel.send('Procesando video')
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
        await context.channel.send('Procesando video')
        var='ffmpeg -loop 1 -i {}output.png -i {}betis.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp', 'output.png', '01.png','output.mp4'))
        

    @commands.command()
    async def communist(self, context, *, user : discord.Member=None):
        # Get user avatar
        avatarUrl=getUser(context,user).avatar_url

        # Create meme
        createMeme(("communist",'01'),avatarUrl,400,(-100,0,0,0),False)

        # Create video
        await context.channel.send('Procesando video')
        var='ffmpeg -loop 1 -i {}output.png -i {}communist.mp3 -filter:v scale=300:-1 -c:v libx264 -framerate 1 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}output.mp4'
        os.system(var.format(memePath,memePath,memePath))
        
        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.mp4"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp', 'output.png', '01.png','output.mp4'))


    @commands.command()
    async def smash(self, context, *, user : discord.Member=None):
        avatarUrl=getUser(context,user).avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",300)

        # variables
        name=str(getUser(context,user))[:-5]  # remove #1234
        txt = "Yiffs into the fight"

        nameX=0
        txtX=8
        imageLayerX=400
        imageLayerY=-40
        avatarX=50
        avatarY=150
        shadowcolor = "black"
        nameColor="white"
        txtColor='orange'

        # Calculate name font size, nameY, txtY depending on name
        var=[150,150,150,150,150,130,130,130,120,120,120,110,110,110,110,110,100,100,90,90,90,90,90] # var[4]=150 text size for a name with 4 chars
        x= symbols('x')
        expr = len(name)*x-var[len(name)]
        sol = solve(expr)
        txtSize=len(name)*sol[0]

        nameY=150-var[len(name)]
        txtY=nameY+var[len(name)]
        

        # Requiremnts
        output= Image.open(memePath+'smash'+'.png').convert("RGBA")
        avatar=Image.open(memePath+'01'+'.png').convert("RGBA")

        txtPic = Image.new('RGBA', (600, 300))
        nameFont = ImageFont.truetype(memePath+'Haettenschweiler-Regular.ttf', txtSize)
        txtFont = ImageFont.truetype(memePath+'Haettenschweiler-Regular.ttf', 70)
        d = ImageDraw.Draw(txtPic)

        ## Drop shadow name
        d.text((nameX+8, nameY+8), name, font=nameFont, fill=shadowcolor)

        # Drop shadow txt
        d.text((txtX+5, txtY+5), txt, font=txtFont, fill=shadowcolor)

        # Put text above drop shadows
        d.text( (nameX, nameY),name, font=nameFont, fill=nameColor)
        d.text( (txtX, txtY),txt, font=txtFont, fill=txtColor)

        # Rotate text and paste it in meme
        w=txtPic.rotate(10, expand=1)
        output.paste(w, (imageLayerX,imageLayerY),  w)
        
        # Paste avatar
        output.paste(avatar, (avatarX,avatarY),  avatar)

        # Save result
        output.save(memePath+'output.png')
     
        await context.channel.send(file=discord.File(memePath+"output.png"))

        await sleep(1)
        deleteRequirements(('01.webp', 'output.png', '01.png'))



    @commands.command()
    async def smash1(self, context, *, user : discord.Member=None):
        avatarUrl=getUser(context,user).avatar_url
        var="wget -O %s%s %s"%(memePath, "01.webp", avatarUrl)
        os.system(var)
        convertPic(memePath+"01.webp","01",1200)


        await context.channel.send('Procesando video')



        # variables
        name=str(getUser(context,user))[:-5]  # remove #1234
        txt = "Yiffs into the figth"

        nameX=0
        txtX=8
        imageLayerX=400
        imageLayerY=-40
        avatarX=50
        avatarY=150
        shadowcolor = "black"
        nameColor="white"
        txtColor='orange'



        video = mp.VideoFileClip(memePath+"smash.mp4")

        logo = (mp.ImageClip(memePath+'01.png')
                    .set_duration(video.duration-6)
                    .set_end('00:00:06.12')
                    .resize(height=2000) # if you need to resize...
                    #.margin(right=8, top=8, opacity=0) # (optional) logo-border padding
                    #.set_pos(("right","top")))
                    .set_pos(lambda t: (-200-t*100, 'center'))
                )
        avatar = (mp.ImageClip(memePath+'01.png')
                    .set_duration(video.duration-8)
                    .set_start('00:00:06.12')
                    .resize(height= lambda t: (1200-t*100))
                    .set_pos((400,150))
                )


        final = mp.CompositeVideoClip([video, logo,avatar])
        final.write_videofile(memePath+"output.mp4")
        final.close()

        await context.channel.send(file=discord.File(memePath+"output.mp4"))
        deleteRequirements(('01.webp', 'output.mp4', '01.png'))



    @commands.command()
    async def impostor(self, context, *, user : discord.Member=None):
        """Quién es el impostor?

        """
        avatarUrl=getUser(context,user).avatar_url
        print(avatarUrl)
        
        createMeme(("impostor",'01'),avatarUrl,205,(0,0,323,175),True)

        # Send meme
        await context.channel.send(file=discord.File(memePath+"output.png"))

        # Delete user avatar and output
        await sleep(1)
        deleteRequirements(('01.webp','output.png','01.png'))

                


def posi(t):
    if t<6:
        return 0.0
    else:
        return 1.0


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

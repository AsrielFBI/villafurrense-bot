import discord
from discord.ext import commands
import asyncio
import random
from gtts import gTTS
import os


class utilities(commands.Cog):
    """Utilidades varias"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def random(self, context,min :int ,max : int , *, user : discord.Member=None):
        """ Genera un número aleatorio

            Uso: fur random                 ---> Genera un numero entre 1 y 100
                 fur random <min> <max>     ---> Genera un numero entre <min> y <max>
        """

        if min and max is not  None:
            num=str(random.randint(min,max))
        else:
            num=str(random.randint(0,100))
        tmp = await context.channel.send('Generando número aleatorio')

        await tmp.edit(content='Generando número aleatorio.')
        await asyncio.sleep(0.2)
        await tmp.edit(content='Generando número aleatorio..')
        await asyncio.sleep(0.2)
        await tmp.edit(content='Generando número aleatorio...')
        await asyncio.sleep(0.2)
        await tmp.edit(content='Generando número aleatorio....')
        await asyncio.sleep(0.2)
        await tmp.edit(content='Generando número aleatorio.....')
        await asyncio.sleep(0.2)

        await tmp.edit(content='Numero aletorio: '+num)



    @commands.command()
    async def txt(self, context, arg,*, user : discord.Member=None):
        """Texto a voz"""
        await context.channel.send("Procesando audio")
        ttmp3 = gTTS(text=arg, lang='es', slow=False)
        ttmp3.save(arg+'.mp3')
        await context.channel.send(file=discord.File(arg+'.mp3'))
        os.system("rm "+arg+'.mp3')



def setup(bot):
    bot.add_cog(utilities(bot))
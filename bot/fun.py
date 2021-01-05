from asyncio.tasks import sleep
import discord
from discord.ext import commands
import random
import asyncio
import os


if os.path.isdir('../fun/Enanas/') :
    enanasPath='../fun/Enanas/'
else:
    enanasPath='/app/fun/Enanas/'


class fun(commands.Cog):
    """Cosas random y divertidas"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def penis(self, context, *, user : discord.Member=None):
        """Buena tula

            Genera un pene de tamaño aleatorio. 
            Uso: 
            fur penis            --> Tu tula
            fur penis @<usuario> --> La tula de @<usuario>
        """
        num=random.randint(1,10)
        output='El pene de {}\n'
        if user==None:
            usuario=context.author.mention
        else:
            usuario=user.mention

        output+='8'
        for x in range(num):
            output+='='
        output+='D'
        await context.channel.send(output.format(usuario))


    @commands.command()
    async def communism(self, context, *, user : discord.Member=None):
        """Serás un comunista bolivariano que apoya al Coletas?
        """
        num=random.randint(0,100)
        output='{} es {}% comunista'
        if user==None:
            usuario=context.author.mention
        else:
            usuario=user.mention
        await context.channel.send(output.format(usuario, num))

    @commands.command()
    async def capitalist(self, context, *, user : discord.Member=None):
        """Serás capitalista y te convertirás en el nuevo lobo de Wall Street?
        """
        num=random.randint(0,100)
        output='{} es {}% capitalista'
        if user==None:
            usuario=context.author.mention
        else:
            usuario=user.mention
        await context.channel.send(output.format(usuario, num))


    @commands.command()
    async def enana(self, context, arg : str=None, *, user : discord.Member=None):
        """Elije una enana o consigue una aleatoria de forma totalmente gratuita
        
            Uso:
                fur enana           ---> Enana aleatoria
                fur enana <palabra> ---> Enana que contega palabra 
        """
        if arg==None:
            output=random.choice(os.listdir(enanasPath))
        else:
            for filenames in os.listdir(enanasPath):
                if arg in filenames.lower():
                    output=filenames
        await context.channel.send(file=discord.File(enanasPath+output), content=output.split(".")[0])


    @commands.command()
    async def enanalist(self, context, *, user : discord.Member=None):
        """Lista todas las enanas existentes"""
        str=os.listdir(enanasPath)
        str[:] = [s.replace('.png', '') for s in str]
        str[:] = [s.replace("'", '') for s in str]
        await context.channel.send(str)

    

def setup(bot):
    bot.add_cog(fun(bot))
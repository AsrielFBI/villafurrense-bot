from asyncio.tasks import sleep
import discord
from discord.ext import commands
import random
import asyncio


class fun(commands.Cog):
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
    async def communist(self, context, *, user : discord.Member=None):
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
    async def ball(self, context, *, user : discord.Member=None):
        tmp =         await context.channel.send( '.')

        for x in range(20):
            
            await tmp.edit(content='   .')
            await asyncio.sleep(.3)
            await tmp.edit(content='.')
            await asyncio.sleep(.3)
        


def setup(bot):
    bot.add_cog(fun(bot))
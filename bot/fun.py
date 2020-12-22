import discord
from discord.ext import commands
import random


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



def setup(bot):
    bot.add_cog(fun(bot))
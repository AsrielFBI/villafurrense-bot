import discord
from discord.ext import commands
import random
import praw

reddit = praw.Reddit(client_id='CLIENT_ID HERE',
                     client_secret='CLIENT_SECRET HERE',
                     user_agent='USER_AGENT HERE')


class animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def penis(self, context, *, user : discord.Member=None):
        """Buena tula

            Genera un pene de tamaño aleatorio
        """
        num=random.randint(1,10)
        output='8'
        for x in range(num):
            output+='='
        output+='D'
        await context.channel.send(output)



def setup(bot):
    bot.add_cog(animal(bot))
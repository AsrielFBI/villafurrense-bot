import discord
from discord.ext import commands
import os

from discord.ext.commands.core import is_owner



if os.path.isfile('~/villafurrense-bot/bot/help.txt') :
    helptxt='~/villafurrense-bot/bot/help.txt'
else:
    helptxt='/app/bot/help.txt'



game="Cosas furries"

class administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def is_owner(ctx):
        return ctx.author.id == 315111397837111296



    # Commands
    @commands.command()
    async def version(self, context, user : discord.Member=None):
        embed=discord.Embed(title="FurBot", description='El mejor bot furro')
        embed.add_field(name='Version', value='V 1.0',inline=False)
        await context.channel.send(embed=embed)



    @commands.command(name='info')
    async def help(context):
        """Muestra la info de Zaffy
        """
        f = open(helptxt, 'r')
        general=f.read()
        await context.channel.send(general)
        f.close()




    #@commands.command()
    #async def online(self, context, *, user : discord.Member=None):
    #    await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(game))






def setup(bot):
    bot.add_cog(administration(bot))

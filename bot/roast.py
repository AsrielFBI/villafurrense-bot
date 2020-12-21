import discord
from discord.ext import commands

class roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='aputo')
    async def aputo(self, context, *, user : discord.Member=None):
        """Asriel puto
        """
        await context.channel.send("Asriel puto")

    @commands.command(name='cputo')
    async def cputo(self, context, *, user : discord.Member=None):
        """Cracker puto
        """
        await context.channel.send("Cracker puto")

    @commands.command(name='tputo')
    async def tputo(self, context, *, user : discord.Member=None):
        """Thedax puto
        """
        await context.channel.send("Thedax puto")

def setup(bot):
    bot.add_cog(roast(bot))
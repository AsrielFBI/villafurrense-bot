import discord
import random
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

    @commands.command(name='insult')
    async def insult(self, context, *, user : discord.Member=None):
        """Insulta gente 7w7

            Genera un insulto aleatorio
        """
        insults=['eres tan fe@ que cuando enviaste tu foto por email la detectó el antivirus']
        insults.append('eres tan fe@ que al nacer el medico dijo: Si no llora es un tumor')
        insults.append('eres tan fe@ que cuando naciste te metieron en una incubadora con cristales tintados')
        insults.append('tu madre era tan gorda que si se ponía un traje amarillo le gritaban taxi')
        insults.append('eres tan torpe que cuando te caíste de la cuna, ya tenías síndrome de down')
        insults.append('eres tan inútil que thedax se volvería independentista solo por no vivir en el mismo país que tú')
        insults.append('das tanto asco que ni los coches bomba de ETA explotarían contigo dentro')
        output='{} %s '%(random.choice(insults))
        await context.channel.send(output.format(user.mention))

def setup(bot):
    bot.add_cog(roast(bot))
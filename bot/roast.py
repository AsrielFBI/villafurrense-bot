import discord
import random
from discord.ext import commands

class roast(commands.Cog):
    """Insultos varios """
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='aputo')
    async def aputo(self, context):
        """Asriel puto
        """
        await context.channel.send("Asriel puto")

    @commands.command(name='cputo')
    async def cputo(self, context):
        """Cracker puto
        """
        await context.channel.send("Cracker puto")


    @commands.command(name='gaputo')
    async def gaputo(self, context):
        """Gala puto
        """
        await context.channel.send("Gala puto")

    @commands.command(name='teputo')
    async def etputo(self, context):
        """Teko puto
        """
        await context.channel.send("Teko puto")

    @commands.command(name='tputo')
    async def tputo(self, context):
        """Thedax puto
        """
        await context.channel.send("Thedax puto")

    @commands.command(name='insult')
    async def insult(self, context, *, user : discord.Member=None):
        """Insulta gente 7w7

            Genera un insulto aleatorio
        """
        if user==None:
            usuario=context.author.mention
        else:
            usuario=user.mention
        insults=['eres tan fe@ que cuando enviaste tu foto por email la detectó el antivirus']
        insults.append('eres tan fe@ que al nacer el medico dijo: Si no llora es un tumor')
        insults.append('eres tan fe@ que cuando naciste te metieron en una incubadora con cristales tintados')
        insults.append('tu madre era tan gorda que si se ponía un traje amarillo le gritaban taxi')
        insults.append('eres tan torpe que cuando te caíste de la cuna, ya tenías síndrome de down')
        insults.append('eres tan inútil que thedax se volvería independentista solo por no vivir en el mismo país que tú')
        insults.append('das tanto asco que ni los coches bomba de ETA explotarían contigo dentro')
        insults.append('das tanto asco que para Alex eres infumable')
        insults.append('eres tan feo que ni los nazis irían a invadirte tu casa')
        output='{} %s '%(random.choice(insults))
        await context.channel.send(output.format(usuario))

def setup(bot):
    bot.add_cog(roast(bot))
import discord
import random
from discord.ext import commands

class roast(commands.Cog):
    """Insultos varios """
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def aputo(self, context):
        """Asriel puto
        """
        await context.channel.send("Asriel puto")


    @commands.command()
    async def aguapo(self, context):
        """Le dices guapo al Asriel
        """
        file = discord.File("stickers/rac.jpg", filename = "rac.jpg")
        await ctx.send("Gracias wapo, feliz navidad" ,file = file)

    @commands.command()
    async def cputo(self, context):
        """Cracker puto
        """
        await context.channel.send("Cracker puto")


    @commands.command()
    async def gaputo(self, context):
        """Gala puto
        """
        await context.channel.send("Gala puto")

    @commands.command()
    async def peputo(self, context):
        """Pen puto
        """
        await context.channel.send("Pen puto")
        
    @commands.command()
    async def teputo(self, context):
        """Teko puto
        """
        await context.channel.send("Teko puto")

    @commands.command()
    async def sliputo(self, context):
        """Sliva puto
        """
        await context.channel.send("Sliva puto")

    @commands.command(name='tputo')
    async def tputo(self, context):
        """Thedax puto
        """
        await context.channel.send("Thedax puto")

    @commands.command()
    async def zaputo(self, context):
        """Zaffy puto
        """
        await context.channel.send("Zaffy puto")

    @commands.command()
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
        insults.append('Tu madre es tan gorda, que cuando le preguntaron por su peso dijeron que no le estaban preguntando por su número de teléfono.')
        insults.append('Tu madre es tan gorda, que las navidades pasadas le hice una foto, y aun se está imprimiendo')
        insults.append('Tu madre es tan gorda y vieja, que cuando dios dijo "QUE SE HAGA LA LUZ" le preguntó a tu madre para apartarse')
        insults.append('Tu madre es tan gorda, que cuando se cayó al suelo nadie se rió, a excepción del suelo que se estaba partiendo')
        insults.append('Tu madre es tan gorda, que cuando no come; Las acciones de comida caen en picado')
        insults.append('Tu madre es tan gorda, que si se compra un abrigo de pieles, se extingue toda una raza')
        output='{} %s '%(random.choice(insults))
        await context.channel.send(output.format(usuario))

def setup(bot):
    bot.add_cog(roast(bot))
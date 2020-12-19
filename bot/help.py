import discord
import os



client = discord.Client()


@client.event
async def getHelp(message):
    text="Usar un sticker: s <nombre_sticker>\nAñadir sticker: Seleccionar una imagen y escribir fur add <nombre_sticker> en la caja de comentario\nVer stickers disponibles: fur list"
    await message.channel.send(text)


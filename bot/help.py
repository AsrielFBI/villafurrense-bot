import discord
import os

client = discord.Client()


@client.event
async def getHelp(message):
    text="Usar un sticker: _<nombre_sticker>\nAñadir sticker: Seleccionar una imagen y escribir *addSticker <nombre_sticker> en la caja de comentario\nVer stickers disponibles: *listStickers"
    await message.channel.send(text)


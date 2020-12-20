import discord
from PIL import Image
import numpy as np
import os

client = discord.Client()
if os.path.isfile('../memes'):
    stickersPath='../memes/'
else:
    stickersPath='/app/memes/'

@client.event
async def test(message):
    """Creates a meme with the user photo

    Args:
        message ([type]): [description]
    """
    img = Image.open("data_mask_1354_2030.png")

    background = Image.open("background_1354_2030.png")

    background.paste(img, (0, 0), img)
    background.save('how_to_superimpose_two_images_01.png',"PNG")
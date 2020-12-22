import discord
from discord.ext import commands
import random
import praw

reddit = praw.Reddit(client_id='pK48pKmt7MTGtA',
                     client_secret='UrsuDb6JQqyrppNb1KA0ezTX5SqDrA',
                     user_agent='prawuwu')


class animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def fox(self, context, *, user : discord.Member=None):
        """Fotos de zorros hermosos -/////-

            Envia una foto de r/foxes
        """
        memes_submissions = reddit.subreddit('foxes').search('flair:"Pics!"') # Gets a random images from r/foxes with flair Pics!
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await context.channel.send(submission.url)



def setup(bot):
    bot.add_cog(animal(bot))
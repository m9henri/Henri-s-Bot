import discord
from discord.ext import commands
import requests

# Variables
version = "2.6.4"
emico = "https://media.discordapp.net/attachments/1179492325957840926/1190400494699552928/IMG_1124.png?ex=65a1a9da&is=658f34da&hm=cf80c472c2fb38010a58d69c13056a714134bdd590ed9e885a4af64b68126b83&=&format=webp&quality=lossless&width=640&height=662"
name = "Henri's bot"

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reddit", help="random reddit post from any subreddit")
    async def reddit(self, ctx, sub):
        response = requests.get(f"https://meme-api.com/gimme/{sub}")
        data = response.json()

        redditURL = data["url"]
        redditName = data["title"]
        redditPoster = data["author"]
        subreddit = data["subreddit"]
        postLink = data["postLink"]
        nsfw = data.get("nsfw", False)

        if nsfw and not ctx.channel.is_nsfw():
            await ctx.send("This post is NSFW and can only be sent in an NSFW channel."
                        )
        else:
            em = discord.Embed(title=redditName, color=discord.colour.Color.yellow())
            em.set_image(url=redditURL)
            em.set_footer(
            text=
            f"Created by: {redditPoster}, subreddit: {subreddit}, post: {postLink}")
            await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(reddit(bot))
import discord
from discord.ext import commands
import requests

# Variables
version = "2.6.4"
emico = "https://media.discordapp.net/attachments/1179492325957840926/1190400494699552928/IMG_1124.png?ex=65a1a9da&is=658f34da&hm=cf80c472c2fb38010a58d69c13056a714134bdd590ed9e885a4af64b68126b83&=&format=webp&quality=lossless&width=640&height=662"
name = "Henri's bot"

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme", help="random meme")
    async def meme(self, ctx):
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()

        memeUrl = data["url"]
        memeName = data["title"]
        memePoster = data["author"]
        memeSub = data["subreddit"]
        memeLink = data["postLink"]

        em = discord.Embed(title=memeName, color=discord.colour.Color.yellow())
        em.set_image(url=memeUrl)
        em.set_footer(
            text=f"Created by: {memePoster}, subreddit: {memeSub}, post: {memeLink}")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(meme(bot))
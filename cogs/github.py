import discord
from discord.ext import commands

class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="github", help="posts the github link")
    async def github(self, ctx):
        await ctx.send("https://github.com/m9henri/Henri-s-Bot")

async def setup(bot):
    await bot.add_cog(github(bot))
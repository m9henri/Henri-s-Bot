import discord, random
from discord.ext import commands

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="gay", help="how gay r u")
    async def gay(self, ctx):
        gay = random.randint(1, 100)
        await ctx.send(f"you are {gay} percent gay")
        if gay == 100:
            await ctx.send("https://tenor.com/view/idubbbz-im-gay-filthy-frank-gif-6128368")

async def setup(bot):
    await bot.add_cog(gay(bot))
import discord, random
from discord.ext import commands

class gay(commands.Cog):
    @commands.command(name="gay", help="how gay r u")
    async def gay(self, ctx):
        gay: int = random.randint(1, 100)
        ctx.send("you are {gay} percent gay")
        if gay == 100:
            ctx.sent("https://tenor.com/view/idubbbz-im-gay-filthy-frank-gif-6128368")

def __init__(self, bot):
    self.bot = bot

async def setup(bot):
    await bot.add_cog(gay(bot))
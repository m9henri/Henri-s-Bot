import discord, random
from discord.ext import commands

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    gay: int = random.randint(1, 100)
    @commands.command(name="gay", help="how gay r u")
    async def gay(self, ctx):
        if gay == 100:
            ctx.send("you are 100 percent gay")
            ctx.sent("https://tenor.com/view/idubbbz-im-gay-filthy-frank-gif-6128368")
        elif gay != 100:
            ctx.send("you are {gay} percent gay")
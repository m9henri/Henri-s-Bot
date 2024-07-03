import discord
from discord.ext import commands
import random

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        n = 1
        while n <= amount:
            result = random.randint(1,size)
            await ctx.send("the result is " + str(result))
            n = (n + 1)



async def setup(bot):
    await bot.add_cog(dice(bot))

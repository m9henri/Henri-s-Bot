import discord, random
from discord.ext import commands

class dice(commands.Cog):
    
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        if amount <= 10:
            while n <= amount:
                n = 1
                result = random.randint(1,size)
                await ctx.send("the result is " + str(result))
                n += 1
        elif amount > 10:
            ctx.send("ran into error: too many dice")

def __init__(self, bot):
    self.bot = bot

async def setup(bot):
    await bot.add_cog(dice(bot))
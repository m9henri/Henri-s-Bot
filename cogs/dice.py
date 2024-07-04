import discord, random
from discord.ext import commands

class dice(commands.Cog):
    
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        if amount <= 10:
            n = 1
            while n <= amount:    
                result = random.randint(1,size)
                await ctx.send(f"result of dice {n} is {result}")
                n += 1
        elif not amount <= 10:
            await ctx.send("ran into error: too many dice, try 10 or less")

def __init__(self, bot):
    self.bot = bot

async def setup(bot):
    await bot.add_cog(dice(bot))
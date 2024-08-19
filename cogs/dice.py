import random
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        n = 1
        while n <= amount:    
            num = random.randint(1, size)
            n += 1
            str: number = ""
            number += f"{num}, "
            await ctx.send({f"results of the dice: {number}"})

async def setup(bot):
    await bot.add_cog(dice(bot))
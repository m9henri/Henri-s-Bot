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
            str: number = f" {num}, "
            if n != 1:
                number += f"{num}, "
            await ctx.send({f"results of the dice: {number}"})
            n += 1
async def setup(bot):
    await bot.add_cog(dice(bot))

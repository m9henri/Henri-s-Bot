import random
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        str: number = f'the result of the {amount} dice is: ' 
        n = 1
        while n <= amount:    
            num = random.randint(1, size)
            number += f" {num}, "
            n += 1
            await ctx.send({{number}"})
async def setup(bot):
    await bot.add_cog(dice(bot))

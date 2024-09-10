import discord, random
import random
from discord.ext import commands

class dice(commands.Cog):
    async def dice(self, ctx, amount: int, size: int):
        n = 1
        # if amount <10:    
            while n <= amount:    
                num = random.randint(1, size)
                await ctx.send({f"results of the dice: {send}"})
                n += 1
            break
        pass
async def setup(bot):
    await bot.add_cog(dice(bot))

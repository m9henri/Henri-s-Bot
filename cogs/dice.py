import discord, random
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="dice", help="random number")
    async def dice(self, ctx, amount: int, size: int):
        n = 1
        while n <= amount:    
            result = random.randint(1, size)
            send = (f"result of dice {n} is ,")
            result2 = send.append(f"{result}, ")
            n += 1
        ctx.send(send)



async def setup(bot):
    await bot.add_cog(dice(bot))
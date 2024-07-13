import discord
from discord.ext import commands
class echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="echo", help="posts the words you tell it to say")
    async def echo(self, ctx, *, echo: str):
        await ctx.send(f"{echo}")

class mock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="mock", help="mock the input")
    async def mock(self, ctx, *, mock: str):
        mocked = "".join(c.upper() if i % 2 else c.lower for i, c in enumerate(mock))
        await ctx.send(f"{mocked}")

class aesthetic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="aesthetic", help="r e p e a t s t h e i n p u t l i k e t h i s")
    async def aesthetic(self, ctx, *, instr: str):
        aesthetic = " ".join(instr)
        await ctx.send(f"{aesthetic}")

async def setup(bot):
    await bot.add_cog(echo(bot))
    await bot.add_cog(mock(bot))
    await bot.add_cog(aesthetic(bot))
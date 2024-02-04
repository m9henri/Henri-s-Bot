import discord
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", help="clear chat")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send("Messages deleted.")

async def setup(bot):
    await bot.add_cog(clear(bot))
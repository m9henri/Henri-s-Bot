import discord
from discord.ext import commands
# clear x # of msgs
class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="clear", help="clear chat")
    async def clear(self, ctx, amount: int):
        if ctx.message.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send("Messages deleted.")
            def __init__(self, bot):
                self.bot = bot
# add cog
async def setup(bot):
    await bot.add_cog(clear(bot))
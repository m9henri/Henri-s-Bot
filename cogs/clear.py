import discord
from discord.ext import commands
# clear x # of msgs
class clear(commands.Cog):
    async def clearuser(self, ctx, user: discord.User):
        if ctx.message.author.guild_permissions.manage_messages:
            @commands.command(name="clear", help="clear chat")
            async def clear(self, ctx, amount: int):
                await ctx.channel.purge(limit=amount + 1)
                await ctx.send("Messages deleted.")
            def __init__(self, bot):
                self.bot = bot
# add cog
async def setup(bot):
    await bot.add_cog(clear(bot))
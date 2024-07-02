import discord
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="ban", help="ban member")
    async def ban(self, ctx, member: discord.Member, reason: str):
        if ctx.message.author.guild_permissions.manage_messages:
            await member.ban(reason=reason)
            await ctx.send(f"User {member.mention} has been banned.")

async def setup(bot):
    await bot.add_cog(ban(bot))
import discord
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", help="ban member")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str):
        await member.ban(reason=reason)
        await ctx.send(f"User {member.mention} has been banned.")

async def setup(bot):
    await bot.add_cog(ban(bot))
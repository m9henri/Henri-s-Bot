import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", help="kick member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason: str):
        await member.kick(reason=reason)

async def setup(bot):
    await bot.add_cog(kick(bot))
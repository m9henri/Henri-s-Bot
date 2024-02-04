import discord
from discord.ext import commands


class add_role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add_role", help="add role to member")
    async def add_role(self, ctx, role: discord.Role, member: discord.Member):
        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been given the {role.name} role!")

async def setup(bot):
    await bot.add_cog(add_role(bot))
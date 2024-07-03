import discord
from discord.ext import commands


class remove_role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove_role", help="add role to member")
    async def add_role(self, ctx, role: discord.Role, member: discord.Member):
        await member.remove_roles(role)
        await ctx.send(f"{author.mention} has takrn the {role.name} role from {member.mention}!")

async def setup(bot):
    await bot.add_cog(remove_role(bot))
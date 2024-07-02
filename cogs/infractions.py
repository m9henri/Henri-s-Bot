import discord
from discord.ext import commands

class infractions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="infractions", help="# of warns")
    async def kick(self, ctx, member: discord.Member):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)
        user_warns_ref = guild_ref.child(f'users/{member.id}/warns')
        user_warns = user_warns_ref.get()
        warns_count = len(user_warns)
        total_warns = len(user_warns_ref.get() or {})
        embed = discord.Embed(
                title=f"{member} has:",
                description=f"Total Warns: {total_warns}",
                color=discord.Color.red())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
# add cog
async def setup(bot):
    await bot.add_cog(infractions(bot))
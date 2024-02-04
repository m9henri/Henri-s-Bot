import discord
from discord.ext import commands

class lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lock(self, ctx):
        
        if ctx.message.author.guild_permissions.manage_channels:
        
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send('channel was locked.')
        else:
            await ctx.send('Missing perms')

async def setup(bot):
    await bot.add_cog(lock(bot))

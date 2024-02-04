import discord
from discord.ext import commands

class unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unlock(self, ctx):
        
        if ctx.message.author.guild_permissions.manage_channels:
            
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send('channel was unlocked.')
        else:
            await ctx.send('Missing perms')

async def setup(bot):
    await bot.add_cog(unlock(bot))

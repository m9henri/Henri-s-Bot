import discord
from discord.ext import commands

class lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lockdown(self, ctx):
        
        if ctx.message.author.guild_permissions.manage_channels:
            
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
            await ctx.send('All channels was locked')
        else:
            await ctx.send('Missing perms')

async def setup(bot):
    await bot.add_cog(lockdown(bot))

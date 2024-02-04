import discord
from discord.ext import commands

class clearuser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clearuser(self, ctx, user: discord.User):
    
        if ctx.message.author.guild_permissions.manage_messages:
        
            await ctx.channel.purge(check=lambda msg: msg.author == user)
            await ctx.send(f'All messages from {user.display_name} was deleted.')
        else:
            await ctx.send('u dont have perms for deleting messages')

async def setup(bot):
    await bot.add_cog(clearuser(bot))


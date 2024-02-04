import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", help="Show ping information.")
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping Information", color=discord.Color.blue())

        # Získání latence bota
        latency = round(self.bot.latency * 1000, 2)
        embed.add_field(name="Bot Latency", value=f"{latency}ms", inline=False)

        # Získání latence zprávy
        msg_latency = round((ctx.message.created_at - ctx.message.created_at).total_seconds() * 1000, 2)
        embed.add_field(name="Message Latency", value=f"{msg_latency}ms", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))

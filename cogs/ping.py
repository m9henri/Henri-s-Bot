import discord
from discord.ext import commands

# variables
emico = "https://cdn.discordapp.com/attachments/1256069941132529674/1257792355151515658/OIP.png?ex=6685b1ea&is=6684606a&hm=b0ccde489363500a4f6593c652825230917f95042411e7ae7ec491e02f292ba5&"
name = "latebncy"

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", help="Show ping information.")
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong!", color=discord.Color.blue())
        embed.set_author(name=name, icon_url=emico)

        # set bot side latency
        latency = round(self.bot.latency * 1000, 2)
        embed.add_field(name="Bot Latency", value=f"{latency}ms", inline=False)

        # set message latency
        msg_latency = round((ctx.message.created_at - ctx.message.created_at).total_seconds() * 1000, 2)
        embed.add_field(name="Message Latency", value=f"{msg_latency}ms", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))

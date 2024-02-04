import discord
from discord.ext import commands

# Variables
version = "2.6.4"
emico = "https://media.discordapp.net/attachments/1179492325957840926/1190400494699552928/IMG_1124.png?ex=65a1a9da&is=658f34da&hm=cf80c472c2fb38010a58d69c13056a714134bdd590ed9e885a4af64b68126b83&=&format=webp&quality=lossless&width=640&height=662"
name = "Henri's bot"

class changelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changelog", help="Display changes")
    async def changelog(self, ctx):  # Added 'self' parameter
        em = discord.Embed(title="Changelog", description=f"{name} v{version}", color=discord.Colour.yellow())  # Fixed typo in 'Colour'
        em.set_author(name=name, icon_url=emico)
        em.add_field(name="Moderation", value="`Message logs`")
        em.add_field(name="Bot", value="`Better error handling, some small improvements, message logs, connection to database, new commands`")
        em.set_footer(text=f"{name} v{version}")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(changelog(bot))


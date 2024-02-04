import discord
from discord.ext import commands

# Variables
version = "2.6.4"
emico = "https://media.discordapp.net/attachments/1179492325957840926/1190400494699552928/IMG_1124.png?ex=65a1a9da&is=658f34da&hm=cf80c472c2fb38010a58d69c13056a714134bdd590ed9e885a4af64b68126b83&=&format=webp&quality=lossless&width=640&height=662"
name = "Henri's bot"

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server_info", help="Show server stats")
    async def server_info(self, ctx):  # Added 'self' parameter
        guild = ctx.guild
        member_count = guild.member_count
        channels = len(guild.channels)
        em = discord.Embed(title=f"Server Info - {guild.name}",
                            color=discord.Color.blue())
        em.add_field(name="Member Count", value=member_count)
        em.add_field(name="Channel Count", value=channels)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(serverinfo(bot))

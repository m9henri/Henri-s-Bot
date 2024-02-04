import discord
from discord.ext import commands

# Variables
version = "2.6.4"
emico = "https://cdn.discordapp.com/attachments/1203494029610717264/1203510979103694918/image.png?ex=65d15bf1&is=65bee6f1&hm=7fc9e85d80e10180aacaae477c2c6e11de5d7ee55a5a3dea2936fda8c738b607&"
name = "evilfluid"


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about", help="Display information about the bot.")
    async def about(self, ctx):
        em = discord.Embed(title="About",
                           description="Bot info",
                           color=discord.Colour.yellow())
        em.set_author(name=name, icon_url=emico)
        em.add_field(name="Created by Marosak09", value="© Marosak09 2022-24")
        em.set_footer(text=f"{name} v{version}")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(about(bot))


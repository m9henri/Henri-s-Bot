import discord
from discord.ext import commands

#variables
index = "."
version = "3.0.0"
emico = "https://media.discordapp.net/attachments/1179492325957840926/1190400494699552928/IMG_1124.png?ex=65a1a9da&is=658f34da&hm=cf80c472c2fb38010a58d69c13056a714134bdd590ed9e885a4af64b68126b83&=&format=webp&quality=lossless&width=640&height=662"
name = "Henri's bot"

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed(title="Help",
                                description="Help with categories",
                                color=discord.Color.gold())
            em.set_author(name=name, icon_url=emico)
            em.add_field(name="Moderation", value="`.help moderation`", inline=False)
            em.add_field(name="Setup", value="`.help setup`", inline=False)
            em.add_field(name="Fun", value="`.help fun`", inline=False)
            em.add_field(name="Other", value="`.help other`", inline=False)
            em.set_footer(text=f"{name} v{version}")
            await ctx.send(embed=em)


    @help.command()
    async def moderation(self, ctx):
        em = discord.Embed(title=" Moderation Help",
                            description="Help with moderation commands",
                            color=discord.Color.blue())
        em.add_field(name="Kick", value="Kick a member: `.kick <user> <reason>`", inline=False)
        em.add_field(name="Ban", value="Ban a member: `.ban <user> <reason>`", inline=False)
        em.add_field(name="Add Role", value="Add role to member: `.add_role <role> <member>`", inline=False)
        em.add_field(name="Clear", value="Clear messages: `.clearuser <user>`", inline=False)
        em.add_field(name="clearuser", value="Clear messages from user: `.clear <msgcount>`", inline=False)
        em.add_field(name="lockdown", value="lock server: `.lockdown`", inline=False)
        em.add_field(name="lock", value="lock current channel: `.lock`", inline=False)
        em.add_field(name="unlock", value="unlock current channel: `.unlock`", inline=False)
        em.add_field(name="Warn", value="Warn member: `.warn <member> <reason>`", inline=False)
        await ctx.send(embed=em)


    @help.command()
    async def setup(self, ctx):
        em = discord.Embed(title="Setup Help",
                            description="Help with setup commands",
                            color=discord.Color.blue())
        em.add_field(name="Server Info", value="Display server info: `.server_info`", inline=False)
        em.add_field(name="Log Room", value="Set log room: `.log_room <#text_channel>`", inline=False)
        em.add_field(name="Warn roles", value="Set warn role: `.warn_role <role>`\nRemove role after warn: `.second_warn_role <role>`", inline=False)
        await ctx.send(embed=em)


    @help.command()
    async def fun(self, ctx):
        em = discord.Embed(title="Fun Help",
                            description="Help with fun commands",
                            color=discord.Color.blue())
        em.add_field(name="Ping", value="Ping the bot: `.ping`", inline=False)
        em.add_field(name="Meme", value="Fetch a meme: `.meme`", inline=False)
        em.add_field(name="Reddit", value="Get a Reddit post: `.reddit <subreddit>`", inline=False)
        em.add_field(name="Custom Command", value="Create custom command: `.createcmd <question> <answer>`\nUse custom command: `.cmd <custom cmd name>`", inline=False)
        await ctx.send(embed=em)


    @help.command()
    async def other(self, ctx):
        em = discord.Embed(title="Other Help",
                            description="Help with other commands",
                            color=discord.Color.blue())
        em.add_field(name="About", value="Show bot info: `.about`", inline=False)
        em.add_field(name="Changelog", value="Show bot changelog: `.changelog`", inline=False)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(help(bot))


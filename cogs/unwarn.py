import discord
from discord.ext import commands
from firebase_admin import credentials, db

# firebase setup
cred = credentials.Certificate("key.json")

# Realtime database initialization
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')

index = "."

class Unwarn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unwarn(self, ctx, member: discord.Member, *, reason: str):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        if ctx.author.guild_permissions.kick_members:
            user_warns_ref = guild_ref.child(f'/users/{member.id}/warns')
            user_warns = user_warns_ref.get()

            if user_warns:
                warns_count = len(user_warns)
                new_warn_number = warns_count - 1
                member.remove_roles(1257378367955669063)
            else:
                new_warn_number = 1
            
            embed = discord.Embed(
                title=f"{member} has been unwarned",
                description=f"New total Warns: {total_warns}",
                color=discord.Color.red())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
            warn_role_id = warn_role_ref.get()
            second_warn_role_id = second_warn_role_ref.get()
        else:
            await ctx.send("You don't have permissions to warn members.")
async def setup(bot):
    await bot.add_cog(Unwarn(bot))
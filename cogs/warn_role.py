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

def get_guild_ref(guild_id):
    return db.reference(f'servers/{guild_id}')

class WarnRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn_role(self, ctx, role: discord.Role):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        warn_role_ref = guild_ref.child('settings/warn_role')

        if warn_role_ref.get():
            old_warn_role_id = warn_role_ref.get()
            old_warn_role = ctx.guild.get_role(old_warn_role_id)

            if old_warn_role:
                await ctx.send(
                    f"Replacing warn role from {old_warn_role.mention} to {role.mention}")
            else:
                await ctx.send(f"Setting warn role to {role.mention}")

        warn_role_ref.set(role.id)
        await ctx.send(f"Warn role set to {role.mention}")

def save_config(guild_id, warn_role):
    if warn_role:
        guild_ref = get_guild_ref(guild_id)
        ref_warn_role = guild_ref.child('settings/warn_role')
        ref_warn_role.set(warn_role.id)

async def setup(bot):
    await bot.add_cog(WarnRole(bot))

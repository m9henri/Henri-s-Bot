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
    return db.reference(f'/servers/{guild_id}')

class RemoveWarnRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.second_warn_role = None  # Přidáváme globální proměnnou pro uchování nastavené role

    @commands.command()
    async def remove_warn_role(self, ctx, role: discord.Role):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        second_warn_role_ref = guild_ref.child('/settings/second_warn_role')

        if second_warn_role_ref.get():
            old_second_warn_role_id = second_warn_role_ref.get()
            old_second_warn_role = ctx.guild.get_role(old_second_warn_role_id)

            if old_second_warn_role:
                await ctx.send(
                    f"Replacing second warn role from {old_second_warn_role.mention} to {role.mention}"
                )
            else:
                await ctx.send(f"Setting second warn role to {role.mention}")

        self.second_warn_role = role
        save_config(guild_id, self.second_warn_role)

        await ctx.send(f"Second Warn role set to {role.mention}")

def save_config(guild_id, second_warn_role):
    if second_warn_role:
        guild_ref = get_guild_ref(guild_id)
        ref_second_warn_role = guild_ref.child('/settings/second_warn_role')
        ref_second_warn_role.set(second_warn_role.id)

async def setup(bot):
    await bot.add_cog(RemoveWarnRole(bot))

import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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


class LogSetup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel = None  # Přidáváme globální proměnnou log_channel

    @commands.command()
    async def log_room(self, ctx, channel: discord.TextChannel):
        if self.log_channel:
            await ctx.send(
                f"Replacing log room from {self.log_channel.mention} to {channel.mention}")
            await self.log_channel.send("This channel has been unassigned as the log room.")
            await self.log_channel.send(embed=discord.Embed(description="Thank you!",
                                                             color=discord.Color.green()))
        self.log_channel = channel
        save_config(self.log_channel)

        await ctx.send(f"Log room is set to: {channel.mention}")


def save_config(log_channel):
    if log_channel:
        guild_id = log_channel.guild.id
        guild_ref = get_guild_ref(guild_id)
        ref_msglog = guild_ref.child('settings/msglog')
        ref_msglog.set(log_channel.id)


async def setup(bot):
    await bot.add_cog(LogSetup(bot))

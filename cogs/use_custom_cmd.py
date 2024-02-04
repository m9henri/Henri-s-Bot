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

class UseCustomCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmd(self, ctx, command_name: str):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        custom_command_ref = guild_ref.child('custom_commands').child(command_name)
        response = custom_command_ref.get()

        if response:
            await ctx.send(response)
        else:
            await ctx.send("Custom command not found!")

async def setup(bot):
    await bot.add_cog(UseCustomCmd(bot))

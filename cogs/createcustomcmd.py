import discord
from discord.ext import commands
import firebase_admin
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


class CreateCustomCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="createcmd", help="create your custom command")
    async def createcmd(self, ctx, command_name: str, response: str):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        custom_command_ref = guild_ref.child('custom_commands').child(command_name)

        # check existence
        if custom_command_ref.get():
            await ctx.send(f"Custom command '{command_name}' already exists!")
        else:
            # create new custom cmd
            custom_command_ref.set(response)
            await ctx.send(f"Custom command '{command_name}' created!")

async def setup(bot):
    await bot.add_cog(CreateCustomCmd(bot))

import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

# firebase setup
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(
    cred, {
        'databaseURL':
        'https://henri-s-bot-default-rtdb.europe-west1.firebasedatabase.app/'
    })

# Realtime database initialization
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')

index = "."

def get_guild_ref(guild_id):
    return db.reference(f'/servers/{guild_id}')

def load_config(guild_id):
    guild_ref = get_guild_ref(guild_id)
    global log_channel
    log_channel_id = guild_ref.child('settings/msglog').get()
    if log_channel_id:
        log_channel = client.get_channel(int(log_channel_id))

# load cogs
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

# activity
@client.event
async def on_ready():
    print("Bot running....")
    await load()
    await client.change_presence(status=discord.Status.do_not_disturb,
                                 activity=discord.Game(f"{index}help"))

# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing arguments, try {index}help")
    else:
        await ctx.send(f"An error occurred: {error}")

# all messages logging
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    save_message_to_db(message)

    if message.content.startswith("."):
        await client.process_commands(message)

def save_message_to_db(message):
    message_content = message.content
    message_channel = message.channel.name
    message_author_name = str(message.author)
    message_author_id = message.author.id
    message_id = message.id
    guild_id = message.guild.id

    # Create a dictionary with the user's tag, message content, and other details
    message_data = {
        "msg_content": message_content,
        "msg_channel": message_channel,
        "author_name": message_author_name,
        "author_id": message_author_id
    }

    try:
        guild_ref = get_guild_ref(guild_id)
        messages_ref = guild_ref.child(f'messages/{message_id}')
        messages_ref.update(message_data)
    except Exception as e:
        print(f"Error saving message to database: {e}")

# Logging deleted messages
@client.event
async def on_message_delete(message):
    guild_id = message.guild.id
    guild_ref = get_guild_ref(guild_id)
    log_channel_id = guild_ref.child('settings/msglog').get()
    if log_channel_id:
        log_channel = client.get_channel(int(log_channel_id))

        deleted_msg_content = message.content
        deleted_msg_author = message.author.name
        deleted_msg_channel = message.channel.name

        embed = discord.Embed(title="Deleted Message Log", color=0xFF0000)
        embed.add_field(name="Author", value=deleted_msg_author, inline=False)
        embed.add_field(name="Channel", value=deleted_msg_channel, inline=False)
        embed.add_field(name="Message", value=deleted_msg_content, inline=False)

        await log_channel.send(embed=embed)

client.run('MTA3NzY4MDkxNjA5MDA3NzI0NA.G0J_Zb.OcWTE1qLiqYJAI2M1HHbA4PX223XNNAnBItrBQ')

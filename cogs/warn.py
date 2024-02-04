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

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason: str):
        guild_id = ctx.guild.id
        guild_ref = get_guild_ref(guild_id)

        if ctx.author.guild_permissions.kick_members:
            user_warns_ref = guild_ref.child(f'/users/{member.id}/warns')
            user_warns = user_warns_ref.get()

            if user_warns:
                warns_count = len(user_warns)
                new_warn_number = warns_count + 1
            else:
                new_warn_number = 1

            warn_data = {"reason": reason, "warned_by": ctx.author.id}
            user_warns_ref.update({f"warn{new_warn_number}": warn_data})

            total_warns = len(user_warns_ref.get() or {})

            embed = discord.Embed(
                title=f"{member} has been warned",
                description=f"Reason: {reason}\nTotal Warns: {total_warns}",
                color=discord.Color.red())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)

            warn_role_threshold_ref = guild_ref.child('/settings/warn_role_threshold')
            warn_role_ref = guild_ref.child('/settings/warn_role')
            second_warn_role_ref = guild_ref.child('/settings/second_warn_role')
            warn_role_id = warn_role_ref.get()
            second_warn_role_id = second_warn_role_ref.get()

            if warn_role_id and second_warn_role_id:
                warn_role_threshold = warn_role_threshold_ref.get() or 3
                if total_warns >= warn_role_threshold:
                    try:
                        role = ctx.guild.get_role(warn_role_id)
                        await member.add_roles(role)
                        await ctx.send(
                            f"{member.mention} has been given the {role.name} role due to reaching {warn_role_threshold} warns."
                        )
                        user_warns_ref.delete()

                        role_to_remove = ctx.guild.get_role(second_warn_role_id)
                        if role_to_remove in member.roles:
                            await member.remove_roles(role_to_remove)
                            await ctx.send(
                                f"{member.mention} has been removed from {role_to_remove.name} role."
                            )
                    except Exception as e:
                        print(f"An error occurred while adding or removing the roles: {e}")
        else:
            await ctx.send("You don't have permissions to warn members.")

def save_config(guild_id, warn_role_threshold, warn_role_id, second_warn_role_id):
    guild_ref = get_guild_ref(guild_id)
    guild_ref.child('/settings/warn_role_threshold').set(warn_role_threshold)
    guild_ref.child('/settings/warn_role').set(warn_role_id)
    guild_ref.child('/settings/second_warn_role').set(second_warn_role_id)

async def setup(bot):
    await bot.add_cog(Warn(bot))

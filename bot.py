import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="!", help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/activate_dev"))
    print(f'Logged in as {bot.user}')

@bot.command(name="help")
async def custom_help(ctx):
    embed = discord.Embed(
        title="Help Menu",
        description="Here's a list of commands available:",
        color=discord.Color.from_rgb(54, 57, 63)  # Discord's default dark mode
    )
    embed.add_field(name="Activate Developer", value="`/activate_dev` - Enable Active Developer badge", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.timestamp = discord.utils.utcnow()
    await ctx.send(embed=embed)

@bot.slash_command(name="activate_dev", description="Enable the Active Developer badge for your account!")
async def activate_dev(ctx):
    embed = discord.Embed(
        description="**Processing...**",
        color=discord.Color.from_rgb(54, 57, 63)
    )
    initial_message = await ctx.respond(embed=embed)
    await asyncio.sleep(2)
    embed = discord.Embed(
        description="**Active Developer Badge Activated!**",
        color=discord.Color.from_rgb(54, 57, 63)
    )
    embed.set_footer(text="Request processed successfully")
    embed.timestamp = discord.utils.utcnow()
    await initial_message.edit_original_response(embed=embed)

bot.run(TOKEN)

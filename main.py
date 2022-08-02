from backend import *
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3 as sl
from backend import *
from typing import Literal
import os
from dotenv import load_dotenv
import datetime
load_dotenv()



#class client(discord.Client):
    #def __init__(self, *, intents: discord.Intents):
        #super().__init__(intents=intents)
        #self.tree = app_commands.CommandTree(self)
    #async def setup_hook(self):
        #self.tree.copy_global_to(guild=discord.Object(id=919047940843143198))
        #await self.tree.sync(guild=discord.Object(id=919047940843143198))
intents = discord.Intents.default()
intents.message_content = True

#bot = client(intents=intents)
bot = commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} and ready to roll')
    print('------')



cogs = [
    "cogs.admin",
]

@bot.command()
@commands.guild_only()
async def load(ctx):
    for cog in cogs:
        await bot.load_extension(cog)
    await ctx.send(f"Loaded!")
@bot.command()
@commands.guild_only()
async def sync(ctx):

    await ctx.bot.tree.sync(guild=discord.Object(id=919047940843143198))
    await ctx.send(f"Synced!")


bot.run(os.getenv('discord_token'))
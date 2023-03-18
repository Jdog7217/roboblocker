from backend import *
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3 as sl
from backend import *
from typing import Literal
import os
import datetime
from discord import Interaction
from discord.app_commands import AppCommandError
cogs = [
    "cogs.admin",
    "cogs.panel",
    "cogs.errors"
]
class client(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents,command_prefix=".")
        #self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        for cog in cogs:
            await bot.load_extension(cog)
        #self.tree.copy_global_to(guild=g)
        await self.tree.sync()

intents = discord.Intents.default()
intents.members = True

bot = client(intents=intents)
# = commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} and ready to roll')
    print('------')




bot.run("MTA4Njc4MDc2MzE0NTUwNjg1Nw.Gjv4pX.C_geBOacSyoDdyjEgcLxZV7RHyVFPuFRfE7ulQ")

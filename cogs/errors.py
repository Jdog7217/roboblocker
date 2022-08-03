
from backend import *
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3 as sl
from typing import Literal
import os
from dotenv import load_dotenv
import datetime
import asyncio

from cogs.admin import admin

class errors(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        bot.tree.on_error = self.app_command_error
    async def app_command_error(self, interaction, error):
        if isinstance(error, app_commands.MissingPermissions):
            embed=discord.Embed(title="Error", description="You are missing permission needed to run this command!", color=discord.Color.red())
            embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
            embed.timestamp = datetime.datetime.utcnow()
            await interaction.response.send_message(embed=embed,ephemeral=True)
        elif isinstance(error, app_commands.BotMissingPermissions):
            embed=discord.Embed(title="Error", description="I dont have permission for this to work!", color=discord.Color.red())
            embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
            embed.timestamp = datetime.datetime.utcnow()
            await interaction.response.send_message(embed=embed,ephemeral=True)
async def setup(bot: commands.Bot):
    await bot.add_cog(errors(bot))
    

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



class client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=919047940843143198))
        await self.tree.sync(guild=discord.Object(id=919047940843143198))
intents = discord.Intents.default()
bot = client(intents=intents)



class verify(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} and ready to roll')
    print('------')

@bot.tree.command()
async def setup(interaction: discord.Interaction):
    await interaction.response.defer()
    server = newserver(interaction.guild.id)
    if server == 0:
        embed=discord.Embed(title="Server added!", description="Server added in our database!", color=discord.Color.green())
        embed.set_footer(text = f"Command ran by {interaction.user.mention}",icon_url=interaction.user.display_icon)
        embed.add_field(name = "Finish setting up your server with /settings!",value = "To delete your servers data please contact CosmicCrow")
        await interaction.response.send_message(embed=embed)
    else:
        embed=discord.Embed(title="Error!", description="It looks like the setup command was already run in the server!", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)
    
bot.run(os.getenv('discord_token'))
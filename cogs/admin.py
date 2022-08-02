from backend import *
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3 as sl
from typing import Literal
import os
from dotenv import load_dotenv
import datetime

class verify(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

class admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="command-1")
    async def my_command(self, interaction: discord.Interaction) -> None:
        """ /command-1 """
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)

    @app_commands.command(name = "setup")
    @app_commands.guilds(discord.Object(id=919047940843143198))
    async def setup(self,interaction: discord.Interaction):
        await interaction.response.defer()
        server = newserver(interaction.guild.id)
        if server == 0:
            embed=discord.Embed(title="Server added!", description="Server added in our database!", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
            embed.add_field(name = "Finish setting up your server with /settings!",value = "To delete your servers data please contact CosmicCrow")
            await interaction.followup.send(embed=embed)
        else:
            embed=discord.Embed(title="Error!", description="It looks like the setup command was already run in the server!", color=discord.Color.red())
            await interaction.followup.send(embed=embed)


    setting = app_commands.Group(name="settings", description="Bot settings", guild_ids=[919047940843143198])

    @setting.command()

    async def all(self, interaction: discord.Interaction) -> None:
        """ Gets all settings """
        server = getserver(interaction.guild.id)
        if server:
            embed=discord.Embed(title="Settings", description="Change a setting with /setting name", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
            embed.add_field(name = "Create a verification panel with /panel",value = f"{':green_square:' if server[2]==True else ':red_square:'} Verification: {'on' if server[2]==True else 'off'}\nLoging Channel: {interaction.guild.get_channel(int(server[4])).mention if server[4]!=None else 'Not set up'}\nRole given when verified: {interaction.guild.get_role(int(server[5])).mention if server[5]!=None else 'Not set up'}")
        else:
            embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)
    
    @setting.command(name="verify") 
    @app_commands.describe(active="When members join they needs to verify. ")
    async def verify(self, interaction: discord.Interaction,active:bool) -> None:
        """ Turns on or off verification """
        change = changesettings(interaction.guild.id,"verify",active)
        if change ==1:
            embed=discord.Embed(title="Settings", description=f"Changed verify to {active}", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        else:
            embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)


    @setting.command(name="channel") # 
    @app_commands.describe(channel="Channel that all logs go to. ")
    async def channel(self, interaction: discord.Interaction,channel:discord.TextChannel=None) -> None:
        """ Changes the logging channel """
        change = changesettings(interaction.guild.id,"channel",channel.id)
        if change ==1:
            embed=discord.Embed(title="Settings", description=f"Changed logging channel to {channel.mention}", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        else:
            embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)


    @setting.command(name="role") 
    @app_commands.describe(role="Role that member gets when they verify")
    async def role(self, interaction: discord.Interaction,role:discord.Role=None) -> None:
        """ Changes the verifacation role """
        change = changesettings(interaction.guild.id,"role",role.id)
        if change ==1:
            embed=discord.Embed(title="Settings", description=f"Changed verifacation role to {role.mention}", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        else:
            embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)

    @setting.command(name="disable") 
    @app_commands.describe(role="Role that member gets when they verify")
    async def role(self, interaction: discord.Interaction,role:discord.Role=None) -> None:
        """ Changes the verifacation role """
        change = changesettings(interaction.guild.id,"role",role.id)
        if change ==1:
            embed=discord.Embed(title="Settings", description=f"Changed verifacation role to {role.mention}", color=discord.Color.green())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        else:
            embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
            embed.set_footer(text = f"Command ran by {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)
async def setup(bot: commands.Bot):
    await bot.add_cog(admin(bot))
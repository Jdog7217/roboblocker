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
user_codes={}


class verify(discord.ui.View):

    def __init__(self,first,second,sign):
        super().__init__(timeout=10)
        self.all = []
        self.num = [x for x in range(9)]
        self.awnswer = 0
        if sign == "-":
            self.awnswer = first-second
        else:
            self.awnswer = first+second
        self.all.append(self.awnswer)
        for i in range(9):
            self.all.append(get_ran(self.all))
        for i in range(10):
            j = random.choice(self.all)
            self.all.remove(j)
            if j == self.awnswer:
                self.buttonr.label = str(j)
            else:
                k = random.choice(self.num)
                self.num.remove(k)
                if k ==1:
                    self.buttonw1.label = j
                elif k ==2:
                    self.buttonw2.label = j
                elif k ==3:
                    self.buttonw3.label = j
                elif k ==4:
                    self.buttonw4.label = j
                elif k ==5:
                    self.buttonw5.label = j
                elif k ==6:
                    self.buttonw6.label = j
                elif k ==7:
                    self.buttonw7.label = j
                elif k ==8:
                    self.buttonw8.label = j
                elif k ==0:
                    self.buttonw9.label = j
        random.shuffle(self._children)


    @discord.ui.button(label="CHANGE_ME1", style=discord.ButtonStyle.blurple)
    async def buttonw1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw1.label,self)

    @discord.ui.button(label="CHANGE_ME2", style=discord.ButtonStyle.blurple)
    async def buttonw2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw2.label,self)

    @discord.ui.button(label="CHANGE_ME3", style=discord.ButtonStyle.blurple)
    async def buttonw3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw3.label,self)

    @discord.ui.button(label="CHANGE_ME4", style=discord.ButtonStyle.blurple)
    async def buttonw4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw4.label,self)

    @discord.ui.button(label="CHANGE_ME5", style=discord.ButtonStyle.blurple)
    async def buttonw5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw5.label,self)

    @discord.ui.button(label="CHANGE_ME6", style=discord.ButtonStyle.blurple)
    async def buttonw6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw6.label,self)

    @discord.ui.button(label="CHANGE_ME7", style=discord.ButtonStyle.blurple)
    async def buttonw7(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw7.label,self)

    @discord.ui.button(label="CHANGE_M8E", style=discord.ButtonStyle.blurple)
    async def buttonw8(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw8.label,self)


    @discord.ui.button(label="CHANGE_M8E", style=discord.ButtonStyle.blurple)
    async def buttonw9(self, interaction: discord.Interaction, button: discord.ui.Button):
        await wrong(interaction,"Incorrect answer!",self.buttonw9.label,self)

    @discord.ui.button(label="CHANGE_ME21", style=discord.ButtonStyle.blurple)
    async def buttonr(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            past = user_codes[interaction.user.id]
            past["failed"] = 2
            user_codes[interaction.user.id] = past
            try:
                user_codes.pop(interaction.user.id)
            except:
                pass
            guild =getserver(interaction.guild.id)
            for child in self.children:
                child.disabled = True
            await self.message.edit(view=self)
            print(guild)
            if guild[5] != None:
                embed=discord.Embed(title="Correct!", description="Giving you roles...", color=discord.Color.orange())
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.response.send_message(embed = embed, ephemeral=True)
                role = interaction.guild.get_role(guild[5])
                await interaction.user.add_roles(role)
                await asyncio.sleep(1)
                embed=discord.Embed(title="Verified", description=f"{role.mention} given!", color=discord.Color.green())
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.edit_original_message(embed=embed)
                
            
            else:
                embed=discord.Embed(title="Verified!", description="You were verified!", color=discord.Color.green())
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.response.send_message(embed = embed, ephemeral=True)
            if guild[4]:
                embed=discord.Embed(title=f"`{interaction.user.name}` was verified!!", description=f"`Reason for verification:` capcha correct", color=discord.Color.green())
                embed.add_field(name = "User details: ",value=f"`Time joined:` {interaction.user.joined_at.strftime('%a, %d %b %Y %I:%M %p')}\n`Account created:` {interaction.user.created_at.strftime('%a, %d %b %Y %I:%M %p')}\n")
                embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                embed.set_image(url="attachment://image.png")
                file = discord.File(f"./images/{interaction.user.id}.png", filename="image.png")
                embed.timestamp = datetime.datetime.utcnow()
                veiw = admin_yes(interaction.user.id)
                veiw.message = await interaction.guild.get_channel(guild[4]).send(embed=embed, file=file,view = veiw)
        except KeyError:
            pass
        for child in self.children:
            child.disabled = True
        await self.message.edit(view=self)
    async def on_timeout(self) -> None:
        for child in self.children:
            child.disabled = True
        await self.message.edit(view=self)
        return await super().on_timeout()


async def wrong(interaction,why,wa,self):
    try:
        past = user_codes[interaction.user.id]
    except:
        past =None
    if past:
        if past["failed"] == 0:
            past["failed"] = 1
            user_codes[interaction.user.id] = past
            embed=discord.Embed(title="Error!", description="That was the wrong answer!! :astonished: \nAre you a bot???", color=discord.Color.red())
            embed.timestamp = datetime.datetime.utcnow()
            msg = await interaction.response.send_message(embed = embed, ephemeral = True)
            guild = getserver(interaction.guild.id)
            user_codes.pop(interaction.user.id)
            if guild[4]:
                embed=discord.Embed(title=f"`{interaction.user.name}` failed verification!", description=f"`Reason for failure:`{why}\n`Answer given:` {wa}", color=discord.Color.red())
                embed.add_field(name = "User details: ", value=f"`Time joined:` {interaction.user.joined_at.strftime('%a, %d %b %Y %I:%M %p')}\n`Account created:` {interaction.user.created_at.strftime('%a, %d %b %Y %I:%M %p')}\n")
                embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                embed.set_image(url="attachment://image.png")
                embed.timestamp = datetime.datetime.utcnow()
                file = discord.File(f"./images/{interaction.user.id}.png", filename="image.png")
                await interaction.user.guild.get_channel(guild[4]).send(embed=embed, file=file)
    for child in self.children:
        child.disabled = True
    await self.message.edit(view=self)


class admin_yes(discord.ui.View,):
    def __init__(self,userid):
        self.user_id = userid
        super().__init__(timeout=20)
    
    @discord.ui.button(label='Kick', style=discord.ButtonStyle.secondary, custom_id='kick')
    async def kick_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("hi")
    @discord.ui.button(label='Ban', style=discord.ButtonStyle.red, custom_id='ban')
    async def ban_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("hi")
    @discord.ui.button(label='Un-Verify', style=discord.ButtonStyle.primary, custom_id='unv')
    async def unv_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("hi")

class verify_panel(discord.ui.View,):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='panel_main')
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if getserver(interaction.guild.id)[6]: 
            try:
                user_codes[interaction.user.id]
                embed=discord.Embed(title="Error", description="Please solve the captcha I already gave you! ", color=discord.Color.red())
                embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.response.send_message(embed=embed, ephemeral=True)

            except KeyError:
                first = random.randint(0,50)
                second = random.randint(0,50)
                sign = random.choice(["-","+"])
                getimage(interaction.user.id,str(first)+sign+str(second))
                embed = discord.Embed(title="Please type the awnser in chat, you have 2 minutes!", description=" ", color=discord.Color.orange())
                file = discord.File(f"./images/{interaction.user.id}.png", filename="image.png")
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_image(url="attachment://image.png")
                awnswer = 0
                if sign == "-":
                    awnswer = first-second
                else:
                    awnswer = first+second
                user_codes[interaction.user.id]={"answer":awnswer,"time":datetime.datetime.utcnow,"failed":0,"channel":interaction.channel.id}
                vy =verify(first,second,sign)
                await interaction.response.send_message(file = file, embed=embed, ephemeral=True,view=vy)
                vy.message = await interaction.original_message()
                await asyncio.sleep(10)
                try:
                    a=user_codes[interaction.user.id]
                except KeyError:
                    a= None
                if a:
                    if a["failed"] == 0:
                        embed=discord.Embed(title="Error", description="2 minutes passed and you still have not solved the problem!! :astonished: \nAre you a bot???", color=discord.Color.red())
                        embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                        embed.timestamp = datetime.datetime.utcnow()


                        await interaction.followup.send(embed=embed, ephemeral=True)
                        guild = getserver(interaction.guild.id)
                        if guild[4]:
                            embed=discord.Embed(title=f"`{interaction.user.name}` failed verification!!!!!", description=f"`Reason:` Timedout after 2 minutes", color=discord.Color.red())
                            embed.timestamp = datetime.datetime.utcnow()
                            embed.add_field(name = "User details: ", value=f"`Time joined:` {interaction.user.joined_at.strftime('%a, %d %b %Y %I:%M %p')}\n`Account created:` {interaction.user.created_at.strftime('%a, %d %b %Y %I:%M %p')}\n")
                            embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                            embed.set_image(url="attachment://image.png")
                            file = discord.File(f"./images/{interaction.user.id}.png", filename="image.png")
                            await interaction.guild.get_channel(guild[4]).send(embed=embed, file=file)
                        user_codes.pop(interaction.user.id)

        else:
            pass

class panels(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    async def cog_load(self) -> None:
        self.bot.add_view(verify_panel())
        
    @app_commands.command(name = "panel")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def panel(self,interaction: discord.Interaction):
        if getserver(interaction.guild.id)[6]: 
            await interaction.response.defer()
            server = getserver(interaction.guild.id)
            if server == 0:
                embed=discord.Embed(title="Error", description="Server not setup!", color=discord.Color.red())
                embed.set_footer(text = f"{interaction.user.name}",icon_url=interaction.user.avatar.url)
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.followup.send(embed=embed)
            else:
                await interaction.followup.send("Creating pannel...",ephemeral=True)
                embed=discord.Embed(title="Anti-bot Verification!", description="Click the button to verify!", color=discord.Color.red())
                await interaction.channel.send(embed=embed,view=verify_panel())
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id in user_codes and False:
            if message.channel.id == user_codes[message.author.id]["channel"] and user_codes[message.author.id]["failed"] == 0:
                if message.content.replace(" ","") == str(user_codes[message.author.id]["answer"]):
                    past = user_codes[message.author.id]
                    past["failed"] = 2
                    user_codes[message.author.id] = past
                    user_codes.pop(message.author.id)
                    guild =getserver(message.guild.id)
                    if guild[5] != None:
                        embed=discord.Embed(title="Correct!", description="Giving you roles...", color=discord.Color.orange())
                        embed.timestamp = datetime.datetime.utcnow()
                        msg = await message.channel.send(embed = embed)
                        role = message.guild.get_role(guild[5])
                        await message.author.add_roles(role)
                        embed=discord.Embed(title="Verified", description=f"{role.mention} given!", color=discord.Color.green())
                        embed.timestamp = datetime.datetime.utcnow()
                        await msg.edit(embed=embed,delete_after=10)
                    else:
                        embed=discord.Embed(title="Correct!", description="Verified!", color=discord.Color.green())
                        embed.timestamp = datetime.datetime.utcnow()
                        msg = await message.channel.send(embed = embed)
                    if guild[4]:
                        embed=discord.Embed(title=f"`{message.author.name}` was verified!!", description=f"`Reason for verification:` capcha given correctly({message.content})", color=discord.Color.red())
                        embed.add_field(name = "User details: ",value=f"`Time joined:` {message.author.joined_at.strftime('%a, %d %b %Y %I:%M %p')}\n`Account created:` {message.author.created_at.strftime('%a, %d %b %Y %I:%M %p')}\n")
                        embed.set_footer(text = f"{message.author.name}",icon_url=message.author.avatar.url)
                        embed.set_image(url="attachment://image.png")
                        file = discord.File(f"./images/{message.author.id}.png", filename="image.png")
                        await message.guild.get_channel(guild[4]).send(embed=embed, file=file)
                else:
                    past = user_codes[message.author.id]
                    past["failed"] = 1
                    user_codes[message.author.id] = past
                    embed=discord.Embed(title="Error!", description="That was the wrong answer!! :astonished: \nAre you a bot???", color=discord.Color.red())
                    embed.timestamp = datetime.datetime.utcnow()
                    msg = await message.channel.send(embed = embed,delete_after=10)
                    guild = getserver(message.guild.id)
                    user_codes.pop(message.author.id)
                    if guild[4]:
                        embed=discord.Embed(title=f"`{message.author.name}` failed verification!", description=f"`Reason for failure:` Wrong answer\n`Answer given:` {message.content}", color=discord.Color.red())
                        embed.add_field(name = "User details: ", value=f"`Time joined:` {message.author.joined_at.strftime('%a, %d %b %Y %I:%M %p')}\n`Account created:` {message.author.created_at.strftime('%a, %d %b %Y %I:%M %p')}\n")
                        embed.set_footer(text = f"{message.author.name}",icon_url=message.author.avatar.url)
                        embed.set_image(url="attachment://image.png")
                        embed.timestamp = datetime.datetime.utcnow()
                        file = discord.File(f"./images/{message.author.id}.png", filename="image.png")
                        await message.guild.get_channel(guild[4]).send(embed=embed, file=file)
                
                        
    
async def setup(bot: commands.Bot):
    await bot.add_cog(panels(bot))
    

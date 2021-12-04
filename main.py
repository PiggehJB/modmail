# README
# All code is explained in tutorial video : https://www.youtube.com/watch?v=ftrTTmwt030

import discord
from discord.ext import commands
import os
from datetime import datetime
from discord.colour import Color
from replit import db

# from keep_alive import keep_alive

def delete_keys():
  for k in db.keys():
    del db[k]

def find_key(id):
  i = False
  for k in db.keys():
    i = True
    return True
  
  if i is False:
    return False
  


token = os.environ['token']
prefix = "."
intents = discord.Intents.all()

bot = commands.Bot(
  command_prefix=prefix,
  case_insensitive=True,
  intents=intents
)

@bot.event
async def on_ready():
  print(f"{bot.user.name} <- Online")

@bot.event
async def on_message(ctx):
  if ctx.author == bot.user:
    return

  guild = bot.get_guild(907412013309894706)
  category = discord.utils.get(guild.categories, id=916765823950012527)
  viewable_role = discord.utils.get(guild.roles, name="Staff")

  # Bot gets dm
  if not ctx.guild:
    pass
  

bot.run(token)

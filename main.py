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

db['key1'] = 'key1'

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
  delete_keys()

@bot.event
async def on_message(ctx):
  if ctx.author == bot.user:
    return

  guild = bot.get_guild(907412013309894706)

  category = discord.utils.get(guild.categories, id=916765823950012527)

  viewable_role = discord.utils.get(guild.roles, name="Staff")

  # Bot gets dm
  if not ctx.guild:
    # Returning user
    if find_key(ctx.author.id) is True:
      channel = bot.get_channel(db[str(ctx.author.id)])

    else:
      try:
        print("New User {}".format(ctx.author.name))
        overwrites = {
          guild.default_role: discord.PermissionOverwrite(read_messages=False),
          viewable_role : discord.PermissionOverwrite(read_messages=True)
        }
        newchannel = await guild.create_text_channel(f"\
        {ctx.author.name}-modmail", overwrites=overwrites, category=category)

        db[str(ctx.author.id)] = newchannel.id
        db[str(newchannel.id)] = ctx.author.id

        channel = bot.get_channel(db[str(ctx.author.id)])
        embed = discord.Embed(title="New DM", color = Color.random(), timestamp = datetime.utcnow(), description=ctx.content)

        embed.set_footer(icon_url=ctx.author.avatar_url, text='\
        Sent by {}'.format(ctx.author.name))
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await channel.send(embed=embed)
        await ctx.add_reaction(emoji='✅')
      except:
        await ctx.add_reaction(emoji='❌')
      

bot.run(token)

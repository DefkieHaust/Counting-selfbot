from discord.ext import commands
bot = commands.Bot(command_prefix="¶")

ch = channel_id_here
token = "token here"

@bot.event
async def on_message(ctx):
  if ctx.author != bot.user and ctx.channel.id == ch:
    try:
      solved = int(eval(ctx.content.split()[0]))
      if solved > 0:
        await ctx.channel.send(solved+1)
    except:
      pass
  
bot.run(token)

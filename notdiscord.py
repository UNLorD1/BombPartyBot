import discord  # importing in discord library
from discord.ext import commands  # enables programming functionality

TOKEN = 'NTU0MjI0NDU4ODc4MTU2ODEw.D39c0g.s32T5763G5h0YedwiPO_15J2i-k'  # unique ID code for bot

bot = commands.Bot(command_prefix='!')  # sets command prefix to !


@bot.event  # discord controls when they're called.
async def on_ready():  # when the bot is done collecting information from discord, servers, etc., do the following:
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):  # displays messages users send on discord
    author = message.author  # captures user
    content = message.content  # captures message
    channel = message.channel  # captures channel
    print('{}: {}: {}'.format(channel, author, content))  # prints author and message on console


# @bot.event
# async def on_message_delete(message):
#     author = message.author  # captures user
#     content = message.content  # captures message
#     channel = message.channel  # captures channel
#     await bot.send_message(channel, '{} tried to delete: {}'.format(author, content))


# @bot.command()
# async def space(ctx):
#     msg = msg_fixer(ctx.message.content)
#     await ctx.send(' '.join(msg))


@bot.command()
async def ping():
    await bot.say('Pong!')


bot.run(TOKEN)

import discord
from discord.ext import commands

TOKEN = NTU0MjI0NDU4ODc4MTU2ODEw.D39c0g.s32T5763G5h0YedwiPO_15J2i-k
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def space(ctx):
    msg = msg_fixer(ctx.message.content)
    await ctx.send(' '.join(msg))

bot.run(TOKEN)
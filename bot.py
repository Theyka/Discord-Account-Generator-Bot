from discord.ext import commands
import os
from ruamel.yaml import YAML
from aioconsole import ainput
from os import listdir
from os.path import isfile, join

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), case_insensitive=True)

yaml = YAML()
with open("config/config.yml", "r") as stream:
	bot.config = yaml.load(stream)

bot.remove_command("help")
for cog in [f for f in listdir("cogs") if isfile(join("cogs", f))]:
	if cog.endswith(".py"):
		try:
			cog = f"cogs.{cog[0:-3]}"
			bot.load_extension(cog)
			print(f"Eklendi - {cog[5:].capitalize()}")
		except Exception as e:
			print(f"Eklenemedi - {cog}: {e}")

async def console():
	cmd = await ainput(">>> ")
	await console()

@bot.event
async def on_ready():
	print("Bot başlatıldı.")
	await console()
    
bot.run(bot.config["token"])

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from lista_de_comandos import lista_de_comandos
from comandos.help import CustomHelp

load_dotenv()

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

# Inicializar o bot
bot = commands.Bot(command_prefix="$", intents=intents, help_command=CustomHelp())

# Registrar os comportamentos do bot
lista_de_comandos(bot)

token = os.getenv("TOKEN")
bot.run(token)

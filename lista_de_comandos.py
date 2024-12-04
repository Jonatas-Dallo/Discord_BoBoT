# Arquivo: components.py
from discord.ext import commands
from comandos.comandos import salve, soma, multiplicar
from comandos.dado import dado

def lista_de_comandos(comando):
    salve(comando)
    soma(comando)
    multiplicar(comando)
    dado(comando)

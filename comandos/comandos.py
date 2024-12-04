from discord.ext import commands

def salve(comando: commands.Bot):
    @comando.command(help="Saúda o bot")
    async def salve(ctx):
        await ctx.send("Salve! Eu sou o bot do BoB.")

def soma(comando: commands.Bot):
    @comando.command(help="Soma dois números.")
    async def soma(ctx, a: int, b: int):
        result = a + b
        await ctx.send(f"O resultado é {result}.")

def multiplicar(comando: commands.Bot):
    @comando.command(help="Multiplica dois números.")
    async def multiplicar(ctx, a: int, b: int):
        result = a * b
        await ctx.send(f"O resultado da multiplicação é {result}.")
        
        
        
        

import random
import re
from discord.ext import commands

def dado(comando: commands.Bot):
    @comando.event
    async def on_message(message):
        if message.author == comando.user:  # Ignora a mensagem do bot
            return
        
        conteudo = message.content
        
        # Caso seja do tipo XdX (exemplo: 2d20)
        if re.match(r'^\d+d\d+$', conteudo):
            vezes, valor_dado = map(int, conteudo.split('d'))
            resultados = [random.randint(1, valor_dado) for _ in range(vezes)]
            resultado_total = sum(resultados)
            await message.channel.send(f"Resultado: *`[{resultado_total}]`* ⟵ {resultados} {conteudo}")
        
        # Caso seja do tipo X#dX (exemplo: 5#d20)
        elif re.match(r'^\d+#d\d+$', conteudo):
            vezes, valor_dado = map(int, conteudo.split('#d'))
            resultados = []
            for _ in range(vezes):
                rolagem = [random.randint(1, valor_dado) for _ in range(valor_dado)]
                resultados.append(rolagem)
            
            for i, resultado in enumerate(resultados, start=1):
                resultado_total = sum(resultado)
                await message.channel.send(f"Resultado {i}: **`[{resultado_total}]`** ⟵ {resultado} {conteudo}")
        
        # Caso seja do tipo X#XdY (exemplo: 2#2d10)
        elif re.match(r'^\d+#\d+d\d+$', conteudo):
            vezes, sub_vezes, valor_dado = map(int, re.findall(r'\d+', conteudo))
            resultados = []
            for _ in range(vezes):
                rolagem = [random.randint(1, valor_dado) for _ in range(sub_vezes)]
                resultados.append(rolagem)
            
            for i, resultado in enumerate(resultados, start=1):
                resultado_total = sum(resultado)
                await message.channel.send(f"Resultado {i}: **`[{resultado_total}]`** ⟵ {resultado} {conteudo}")
        
        # Não se esqueça de processar os outros comandos do bot (caso haja outros)
        await comando.process_commands(message)

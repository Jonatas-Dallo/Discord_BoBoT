import random
import re
from discord.ext import commands

def dado(comando: commands.Bot):
    @comando.event
    async def on_message(message):
        if message.author == comando.user:  # Ignora mensagens do bot
            return

        conteudo = message.content.strip()
        usuario = message.author.display_name

        def formatar_resultado(rolagem, valor_dado):
            return f"**` {rolagem} `**" if rolagem in {1, valor_dado} else f"` {rolagem} `"
        
        def formatar_resultado2(rolagem, valor_dado):
            return f"**{rolagem}**" if rolagem in {1, valor_dado} else f"{rolagem}"

        # Caso seja do tipo dX (exemplo: d20)
        if re.match(r'^d\d+$', conteudo):
            valor_dado = int(conteudo[1:])
            resultado = random.randint(1, valor_dado)
            resultado_formatado = formatar_resultado(resultado, valor_dado)
            await message.channel.send(f"{usuario} rolou: \n[ {resultado_formatado} ] ⟵ {conteudo}", 
                reference=message)

        # Caso seja do tipo XdX (exemplo: 2d20)
        elif re.match(r'^\d+d\d+$', conteudo):
            vezes, valor_dado = map(int, conteudo.split('d'))
            resultados = [random.randint(1, valor_dado) for _ in range(vezes)]
            resultados_formatados = [formatar_resultado2(r, valor_dado) for r in resultados]
            resultado_total = sum(resultados)
            await message.channel.send(
                f"{usuario} rolou: \n[**` {resultado_total} `**] ⟵ [ {', '.join(resultados_formatados)} ] {conteudo}", 
                reference=message
            )
            
        # Caso seja do tipo X#dY (exemplo: 2#d20)
        elif re.match(r'^\d+#d\d+$', conteudo):
            vezes, valor_dado = map(int, conteudo.split('#d'))
            resultados = [random.randint(1, valor_dado) for _ in range(vezes)]

            resultado_texto = "\n".join(
                f"`⠀{resultado}⠀`  ⟵ [ {formatar_resultado2(resultado, valor_dado)} ] d{valor_dado}"
                for resultado in resultados
            )
            await message.channel.send(f"Resultado de {usuario} para {conteudo}:\n\n{resultado_texto}", 
                reference=message)

        # Caso seja do tipo X#XdY (exemplo: 2#2d10)
        elif re.match(r'^\d+#\d+d\d+$', conteudo):
            vezes, sub_vezes, valor_dado = map(int, re.findall(r'\d+', conteudo))
            resultados = []
            for _ in range(vezes):
                rolagem = [random.randint(1, valor_dado) for _ in range(sub_vezes)]
                resultados.append(rolagem)

            resultado_texto = "\n".join(
                f"`⠀{sum(resultado)}⠀`  ⟵ [ {', '.join(formatar_resultado2(r, valor_dado) for r in resultado)} ] d{valor_dado}"
                for resultado in resultados
            )
            await message.channel.send(f"Resultado de {usuario} para {conteudo}:\n\n{resultado_texto}", 
                reference=message)

        # Processa outros comandos
        await comando.process_commands(message)

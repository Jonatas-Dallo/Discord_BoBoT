from discord.ext import commands

class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        """Envia a mensagem de ajuda do bot, incluindo uma listagem dos comandos."""
        help_message = "Aqui estão os comandos disponíveis:\n\n"
        # Ordenar os comandos (para exibir na ordem que você deseja)
        commands_list = []
        for cog, commands in mapping.items():
            if commands:  # Se houver comandos na categoria
                cog_name = cog.qualified_name if cog else "Comandos"
                for command in commands:
                    commands_list.append(f"**`${command.name}`** - {command.help}")  # Adicionando $ antes do comando
        # Ordenar os comandos por nome
        commands_list.sort()

        # Adicionando os comandos à mensagem
        help_message += "\n".join(commands_list)

        # Traduzindo a descrição do comando `help`
        help_message = help_message.replace("**`$help`** - Shows this message", "**$help** - Exibe esta mensagem")
        print(help_message)

        await self.get_destination().send(help_message)

    async def send_command_help(self, command):
        """Envia a ajuda de um comando específico."""
        help_message = f"**`{command.name}`** - {command.help}"
        await self.get_destination().send(help_message)

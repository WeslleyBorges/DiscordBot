import discord
import asyncio
import strings_codes
import auxiliary_functions


client = discord.Client()


@client.event
async def on_ready():
    print('Estou pronto, mas não aviso no chat.')


@client.event
async def on_message(message):
    # ADICIONAR UMA VERIFICAÇÃO PARA VER SE O BOT ESTÁ CAPTURANDO SUAS PRÓPRIAS MENSAGENS
        lower_command = message.content.lower()

        if lower_command.startswith('!'):
            await client.send_message(message.channel, auxiliary_functions.switch_command(message))
        else:
            await client.send_message(message.channel, strings_codes.invalid_commands['wrong_prefix'])

client.run(strings_codes.colossal_token)



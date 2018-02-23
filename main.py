import discord
import asyncio
import strings_codes
import auxiliary_functions

client = discord.Client()


@client.event
async def on_ready():
    await client.send_message(client.get_channel(strings_codes.test_channel_id), strings_codes.welcome_message)


@client.event
async def on_message(message):
    # ADICIONAR UMA VERIFICAÇÃO PARA VER SE O BOT ESTÁ CAPTURANDO SUAS PRÓPRIAS MENSAGENS
        lower_command = message.content.lower()

        if lower_command.startswith('!'):
            await client.send_message(message.channel, auxiliary_functions.switch_command(message))
        else:
            await client.send_message(message.channel, strings_codes.invalid_commands['wrong_prefix'])

client.run(strings_codes.colossal_token)



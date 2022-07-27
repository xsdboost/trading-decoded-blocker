import discord
from discord.ext.commands import Bot
from bantools.use_cases.listeners import find_references
from bantools.utils.configtools import Config
from bantools.use_cases.listeners import search_for_references


def main():

    intents = discord.Intents.default()
    intents.members = True

    config = Config(project_name="bantools", config_resource="resources/config.yaml")

    validator = Bot(command_prefix=["/tc-", "/"], intents=intents)
    validator.add_listener(search_for_references, "on_message")
    validator.add_command(find_references)

    validator.run(config.account_key)


if __name__ == "__main__":
    main()

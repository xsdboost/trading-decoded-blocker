import discord
from discord.ext.commands import Bot

from bantools.utils.configtools import Config
from bantools.use_cases.listeners import usecase_did_user_already_signup


def main():

    config = Config(project_name="bantools", config_resource="resources/config.yaml")

    intents = discord.Intents.default()
    intents.members = True

    new_account_validator = Bot(command_prefix="-", intents=intents)
    new_account_validator.add_listener(usecase_did_user_already_signup, "on_message")

    new_account_validator.run(config.account_key)


if __name__ == "__main__":
    main()

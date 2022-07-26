import discord
from discord.ext.commands import Bot, Context
from bantools.utils.configtools import Config
from bantools.use_cases.listeners import usecase_did_user_already_signup, search_for_references


def main():

    intents = discord.Intents.default()
    intents.members = True

    config = Config(project_name="bantools", config_resource="resources/config.yaml")

    validator = Bot(command_prefix="/", intents=intents)
    validator.add_listener(usecase_did_user_already_signup, "on_message")

    @validator.command(pass_context=True, aliases=['trialsearch'])
    async def chickennuggets(ctx: Context, username: str):
        await search_for_references(ctx.guild, username, config)

    validator.run(config.account_key)


if __name__ == "__main__":
    main()

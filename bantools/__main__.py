from discord.ext.commands import Bot
from bantools.use_cases.listeners import usecase_did_user_already_signup
from bantools.utils.envtools import getenv_variable


def main():

    banningTools = Bot(command_prefix="/")
    banningTools.add_listener(usecase_did_user_already_signup, "on_member_join")
    banningTools.run(getenv_variable("API_KEY"))


if __name__ == "__main__":
    main()

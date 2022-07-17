from discord.ext.commands import Bot

from bantools.use_cases.listeners import usecase_did_user_already_signup
from bantools.utils.envtools import getenv_variable


def main():
    account_key = getenv_variable("API_KEY")

    new_account_validator = Bot(command_prefix="-")
    new_account_validator.add_listener(usecase_did_user_already_signup, "on_member_join")

    new_account_validator.run(account_key)

if __name__ == "__main__":
    main()

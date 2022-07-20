import os.path

from discord.ext.commands import Bot
from bantools.utils.configtools import get_config, ConfigType
from bantools.use_cases.listeners import usecase_did_user_already_signup


def main():
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    config = get_config(ConfigType.BAN, config_file_path, "test_server")

    new_account_validator = Bot(command_prefix="-")
    new_account_validator.add_listener(
        usecase_did_user_already_signup, "on_member_join"
    )

    new_account_validator.run(config.account_key)


if __name__ == "__main__":
    main()

from functools import partial
from typing import List, Optional

from bantools.domain.parsers import new_user_logger_parser_rule_001
from bantools.repositories.discord import DiscordChannelRepository, MessageContent


def name_in_text(member_name: str, message: MessageContent) -> bool:
    """

    This function contains business logic for determining if the member is referenced in the text

    Parameters
    ----------
    member_name: str
        memeber name that we will check for in text

    message: MessageContent
        Required content of discord message

    Returns
    -------

    """
    if member_name.lower() == new_user_logger_parser_rule_001(message.text_content).lower():
        return True
    else:
        return False


async def get_member_reference_in_channel(
    member_name: str, channel_name: str, discord_repo: DiscordChannelRepository
) -> Optional[List[MessageContent]]:
    """
    Parameters
    ----------
    member_name : str
        member to search in repo

    channel_name: str
        channel name

    discord_repo : DiscordChannelRepository
        discord repo that we will be sourcing from

    Returns
    -------
    List[MessageContent]
        generic message objects returned  containing the required components from message containing member name

    Raises
    ------


    """

    entries: Optional[List[MessageContent]] = await discord_repo.fetch_messages(
        channel_name, 1000
    )

    name_has_text = partial(name_in_text, member_name)

    return list(filter(name_has_text, entries))

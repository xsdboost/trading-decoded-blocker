import functools as func
from typing import List, Optional

from bantools.domain import parser
from bantools.repositories.discord import DiscordChannelRepository, MessageContent


def filter_rule_contains_name(search_text: str, message: MessageContent) -> bool:
    """

    This function contains business logic for determining if the member is referenced in the text

    Parameters
    ----------
    search_text: str
        memeber name that we will check for in text

    message: MessageContent
        Required content of discord message

    Returns
    -------

    """

    """ Rule: text_content is a command """
    if message.text_content.strip().startswith("/"):
        return False
    elif search_text == parser.new_user_logger_rule_001(message.text_content):
        return True
    else:
        return False


async def get_member_reference_in_channel(
    search_text: str, channel_name: str, discord_repo: DiscordChannelRepository
) -> List[MessageContent]:
    """
    Parameters
    ----------
    search_text : str
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
        channel_name, 5000
    )

    return list(filter(func.partial(filter_rule_contains_name, search_text), entries))

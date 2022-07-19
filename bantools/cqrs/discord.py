from typing import List, Optional

from bantools.globals import CHANNEL_TO_SEARCH
from bantools.repositories.discord import DiscordChannelRepository, MessageContent


def get_member_reference_in_channel(
    member_name: str, discord_repo: DiscordChannelRepository
) -> List[MessageContent]:
    """
    Parameters
    ----------
    member_name : str
        member to search in repo

    discord_repo : DiscordChannelRepository
        discord repo that we will be sourcing from

    Returns
    -------
    List[MessageContent]
        generic message objects returned  containing the required components from message containing member name

    Raises
    ------


    """
    def name_in_text(message: MessageContent):
        if member_name.lower() in message.text_content.lower().split():
            return True
        else:
            return False

    entries: Optional[List[MessageContent]] = await discord_repo.fetch_messages(CHANNEL_TO_SEARCH, 1000)

    return list(filter(name_in_text, entries))

from typing import List

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

    pass

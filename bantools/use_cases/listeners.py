import os
from typing import List

from discord.member import Member
from discord.message import Message
from bantools.cqrs.discord import get_member_reference_in_channel
from bantools.domain.userinfo import (
    MessageAttrib,
    get_user_references_in_message_list,
    count_references_of_memeber,
    MemberReferenceCount,
)
from bantools.messaging_content import warning_channel as messaging
from bantools.utils.configtools import get_config, ConfigType
from bantools.repositories.communications import ChannelCommunicator
from bantools.repositories.discord import DiscordChannelRepository, MessageContent


async def usecase_did_user_already_signup(message: Message) -> None:
    """

    This callable usecase determines if the newly joining member already joined and left

    Parameters
    ----------
    member: Member
        discord Member

    Returns
    -------
    None

    Raises
    ------

    """
    config_file_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
    config = get_config(ConfigType.BAN, config_file_path)

    if message.channel.name != config.searching_channel:
        return

    """
    
    Note: if we are reacting to messages sent to the channel then we need to 
    parse the message to get the memeber from it's content 
    
    """
    member = message.author

    discord_repo = DiscordChannelRepository(member.guild)
    logger = ChannelCommunicator(member.guild, config.reporting_channel)

    messages: List[MessageContent] = await get_member_reference_in_channel(
        member.display_name, config.searching_channel, discord_repo
    )

    user_message_entries: List[MessageAttrib] = get_user_references_in_message_list(
        messages
    )

    signup_count: MemberReferenceCount = count_references_of_memeber(
        user_message_entries, member.display_name
    )

    if signup_count.count > 1:
        await logger.send(messaging.offender_found(signup_count))

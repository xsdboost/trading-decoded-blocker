from typing import List, Optional

from discord import Guild
from discord.message import Message
from bantools.cqrs.discord import get_member_reference_in_channel
from bantools.domain import parser
from bantools.domain.userinfo import (
    MessageAttrib,
    get_user_references_in_message_list,
    count_references_of_memeber,
    MemberReferenceCount,
)
from bantools.messaging import warning_text as messaging
from bantools.utils.configtools import Config
from bantools.messaging.communications import ChannelCommunicator
from bantools.repositories.discord import DiscordChannelRepository, MessageContent


async def search_for_references(guild: Guild, member_name: str, config: Config) -> None:
    """
    This callable usecase determines if the newly joining member already joined and left

    Parameters
    ----------
    guild: Guild
        Server Guild

    member_name: str
        the member name being searched for

    config: Config
        runtime configuration

    Returns
    -------

    """
    discord_repo = DiscordChannelRepository(guild)
    logger = ChannelCommunicator(guild, config.reporting_channel)

    messages: List[MessageContent] = await get_member_reference_in_channel(
        member_name, config.watch_channel, discord_repo
    )

    user_message_entries: List[MessageAttrib] = get_user_references_in_message_list(
        messages
    )

    signup_count: MemberReferenceCount = count_references_of_memeber(
        user_message_entries
    )

    if signup_count is not None and signup_count.count > 1:
        await logger.send(messaging.offender_found(signup_count))


async def usecase_did_user_already_signup(message: Message) -> None:
    """

    Parameters
    ----------
    message: Message
        Message sent to any channel

    Returns
    -------
    None

    Raises
    ------

    """
    config = Config(project_name="bantools", config_resource="resources/config.yaml")

    if message.channel.name != config.watch_channel:
        return

    """

    Note: if we are reacting to messages sent to the channel then we need to
    parse the message to get the memeber name from it's content

    """

    guild = message.author.guild
    member_name = parser.new_user_logger_rule_001(message.content)

    await search_for_references(guild, member_name, config)


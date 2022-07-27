from typing import List, Optional

from discord import Guild
from discord.ext import commands
from discord.ext.commands import Context
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


async def usecase_did_user_already_signup(
    discord_repo: DiscordChannelRepository, member_name: str, config: Config
) -> MemberReferenceCount:
    """
    This callable usecase determines if the newly joining member already joined and left

    Parameters
    ----------
    discord_repo: DiscordChannelRepository
        discord channel you will source from

    member_name: str
        the member name being searched for

    config: Config
        runtime configuration

    Returns
    -------

    """

    messages: List[MessageContent] = await get_member_reference_in_channel(
        member_name, config.watch_channel, discord_repo
    )

    user_message_entries: List[MessageAttrib] = get_user_references_in_message_list(
        messages
    )

    return count_references_of_memeber(user_message_entries)


async def search_for_references(message: Message) -> None:
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

    guild: Guild = message.guild
    discord_repo = DiscordChannelRepository(guild)
    logger = ChannelCommunicator(guild, config.reporting_channel)

    """

    Note: if we are reacting to messages sent to the channel then we need to
    parse the message to get the memeber name from it's content

    """

    member_name = parser.new_user_logger_rule_001(message.content)

    signup_count: MemberReferenceCount = await usecase_did_user_already_signup(
        discord_repo, member_name, config
    )

    if signup_count is not None and signup_count.count > 1:
        await logger.send(messaging.offender_found(signup_count))


@commands.command(name="verif", aliases=["check", "tf", "tc"])
async def find_references(ctx: Context, member_name: str) -> None:
    """

    Parameters
    ----------
    ctx: Context
        discord context

    member_name: str
        member_name searched

    Returns
    -------
    None

    Raises
    ------

    """
    config = Config(project_name="bantools", config_resource="resources/config.yaml")

    if ctx.channel.name == config.reporting_channel:
        return

    guild: Guild = ctx.guild
    discord_repo = DiscordChannelRepository(guild)
    logger = ChannelCommunicator(guild, config.reporting_channel)

    """

    Note: if we are reacting to messages sent to the channel then we need to
    parse the message to get the memeber name from it's content

    """
    signup_count: MemberReferenceCount = await usecase_did_user_already_signup(
        discord_repo, member_name, config
    )

    if signup_count is None:
        await logger.send(messaging.nothing_found(member_name))
    else:
        await logger.send(messaging.offender_found(signup_count))

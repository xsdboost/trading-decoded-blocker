from dataclasses import dataclass
from datetime import datetime
from typing import List

from discord import Guild, Message, TextChannel, utils
from discord.ext.commands import Bot

MAX_MESSAGE_FETCH = 1000


@dataclass
class MessageContent:
    id: int
    text_content: str
    guild_id: int
    channel_id: int
    create_at: datetime
    message_url: str


def convert_to_generic_metric(message: Message) -> MessageContent:
    """
    Parameters
    ----------
    message: Message
        discord messages to convert

    Returns
    -------
    MessageContent
        discord message content encapsulated into generic message format

    Raises
    ------

    """

    return MessageContent(
        message.id,
        message.content,
        message.guild.id,
        message.channel.id,
        message.created_at,
        message.jump_url,
    )


def to_generic_messages(messages: List[Message]) -> List[MessageContent]:
    """
    Parameters
    ----------
    messages: List[Message]
        list of discord messages to convert

    Returns
    -------
    List[MessageContent]
        list of message converted to generic message type fetch from channel

    Raises
    ------


    """

    generic_messages = list()

    for message in messages:
        content = convert_to_generic_metric(message)
        generic_messages.append(content)

    return generic_messages


class DiscordChannelRepository:
    def __init__(self, bot: Bot, guild: Guild) -> None:

        self.coreBot: Bot = bot
        self.guild: Guild = guild

    async def fetch_messages(
        self, channel_name: str, row_limit: int = MAX_MESSAGE_FETCH
    ) -> List[MessageContent]:
        """
        Parameters
        ----------
        channel_name: str
            dicord channel we will  fetch the data from

        row_limit: int = MAX_MESSAGE_FETCH
            the limit of records to fetch

        Returns
        -------
        List[MessageContent]
            list of message converted to generic message type fetch from channel

        Raises
        ------


        """

        if row_limit > MAX_MESSAGE_FETCH:

            channel_id = utils.get(self.guild.channels, name=channel_name)
            channel: TextChannel = self.coreBot.get_channel(channel_id)
            messages: List[Message] = await channel.history(limit=channel_id).flatten()
            generic_msgs = to_generic_messages(messages)

            return generic_msgs

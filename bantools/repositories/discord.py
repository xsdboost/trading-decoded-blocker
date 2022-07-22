from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from discord import Guild, Message, TextChannel, utils

global_channel_fetch_size = 1000


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
    def __init__(self, guild: Guild) -> None:

        self.guild: Guild = guild

    def _get_channel_by_name(self, channel_name: str) -> TextChannel:
        return utils.get(self.guild.channels, name=channel_name)

    async def fetch_messages(
        self, channel_name: str, entry_limit: int = global_channel_fetch_size
    ) -> Optional[List[MessageContent]]:
        """
        Parameters
        ----------
        channel_name: str
            dicord channel we will  fetch the data from

        entry_limit: int = MAX_MESSAGE_FETCH
            the limit of records to fetch

        Returns
        -------
        List[MessageContent]
            list of message converted to generic message type fetch from channel

        Raises
        ------

        """

        entry_limit = (
            entry_limit
            if entry_limit > global_channel_fetch_size
            else global_channel_fetch_size
        )

        channel = self._get_channel_by_name(channel_name)
        messages: List[Message] = await channel.history(limit=entry_limit).flatten()

        return to_generic_messages(messages)

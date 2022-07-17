from abc import ABC, abstractmethod
from datetime import datetime

from discord.ext.commands import Bot
from discord import TextChannel, Message, Guild
from dataclasses import dataclass
from typing import List

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
    return MessageContent(
        message.id,
        message.content,
        message.guild.id,
        message.channel.id,
        message.created_at,
        message.jump_url,
    )


def to_generic_messages(messages: List[Message]) -> List[MessageContent]:
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
        self, channel_id: int, row_limit: int = MAX_MESSAGE_FETCH
    ) -> List[MessageContent]:

        if row_limit > MAX_MESSAGE_FETCH:

            channel: TextChannel = self.coreBot.get_channel(channel_id)
            messages: List[Message] = await channel.history(limit=channel_id).flatten()
            generic_msgs = to_generic_messages(messages)

            return generic_msgs

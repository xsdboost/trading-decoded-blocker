from dataclasses import dataclass
from datetime import datetime
from typing import List, Any
from discord.member import Member

from bantools.repositories.communications import ChannelCommunicator
from bantools.repositories.discord import DiscordChannelRepository, MessageContent
from bantools.messaging import warning_channel as messaging
from bantools.globals import CHANNEL_TO_REPORT, CHANNEL_TO_SEARCH
from bantools.cqrs.discord import (
    get_member_reference_in_channel,
)


@dataclass
class MemberReferenceCount:
    member_name: str
    count: int
    references: List[str]

@dataclass
class MessageAttrib:
    member_id: int
    member_content: str
    message_created: datetime
    message_url: str

    def __post_init__(self) -> None:
        self.member_content_referenced: str = self.parse_user(self.member_content)

    def parse_user(self, full_content: str) -> str:
        return full_content.split()[0]


def count_references_of_memeber(
    message_entries: List[MessageAttrib], member_name: str
) -> MemberReferenceCount:

    count: int = 0
    ref_urls: List[str] = list()

    for message in message_entries:
        if message.member_content_referenced == member_name:
            count = count + 1
            ref_urls.append(message.message_url)

    return MemberReferenceCount(member_name, count, ref_urls)


def get_user_references_in_message_list(
    messages: List[MessageContent],
) -> List[MessageAttrib]:

    message_attribs: List[MessageAttrib] = list()
    for message in messages:
        attrib = MessageAttrib(message.id, message.text_content, message.create_at)
        message_attribs.append(attrib)

    return message_attribs


def usecase_did_user_already_signup(member: Member) -> None:

    discord_repo = DiscordChannelRepository(member.bot, member.guild)
    warning_channel = ChannelCommunicator(member.bot, CHANNEL_TO_REPORT)

    messages: List[MessageContent] = get_member_reference_in_channel(
        member.display_name, discord_repo
    )

    user_message_entries: List[MessageAttrib] = get_user_references_in_message_list(
        messages
    )

    signup_count: MemberReferenceCount = count_references_of_memeber(
        user_message_entries, member.display_name
    )

    if signup_count.count > 1:
        message = messaging.offender_found(signup_count)
        warning_channel.send(message)

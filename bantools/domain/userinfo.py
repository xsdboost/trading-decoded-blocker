from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from bantools.domain import parser
from bantools.repositories.discord import MessageContent


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

        self.member_name: str = parser.new_user_logger_rule_001(self.member_content)


def count_references_of_memeber(
    message_entries: Optional[List[MessageAttrib]],
) -> Optional[MemberReferenceCount]:
    """
    Parameters
    ----------
    message_entries: List[MessageAttrib]
        stats of attributes from discord message

    Returns
    -------
    MemberReferenceCount
        returns reference count object containing member_name, counts of occurances, and reference to jump_urls

    Raises
    ------

    """
    if message_entries is None or len(message_entries) == 0:
        return None

    count: int = 0
    ref_urls: List[str] = list()
    for message in message_entries:
        count = count + 1
        ref_urls.append(message.message_url)

    return MemberReferenceCount(message_entries[0].member_name, count, ref_urls)


def get_user_references_in_message_list(
    messages: Optional[List[MessageContent]],
) -> Optional[List[MessageAttrib]]:
    """
    Parameters
    ----------
    messages: List[MessageContent]
        Generic messages content

    Returns
    -------
    MemberReferenceCount
        get attributes from message

    Raises
    ------

    """
    if messages is None or len(messages) == 0:
        return None

    message_attribs: List[MessageAttrib] = list()
    for message in messages:
        attrib = MessageAttrib(
            message.id, message.text_content, message.create_at, message.message_url
        )
        message_attribs.append(attrib)

    return message_attribs

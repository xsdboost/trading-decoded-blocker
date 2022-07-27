from dataclasses import dataclass
from typing import List
from bantools.use_cases.listeners import MemberReferenceCount


@dataclass
class Field:
    name: str
    value: str


@dataclass
class OfferMessage:
    description: str
    reference_links: List[Field]


def nothing_found(member_name: str) -> OfferMessage:
    """

    Parameters
    ----------
    member_name: str
        Member name that was searched

    Returns
    -------
    Returns embed message specifying no results
    """
    return OfferMessage(f"No entries found for user: **{member_name}**\n", [])


def offender_found(member_reference: MemberReferenceCount) -> OfferMessage:
    """
    Parameters
    ----------
    member_reference: MemberReferenceCount
        A member count and reference object containing instance of name in chat

    Returns
    -------
    str
        Creates a discord chat friendly text message reporting the offender

    Raises
    ------


    """

    fields: List[Field] = list()
    for ref_id, reference in enumerate(member_reference.references, start=1):
        field = Field(name=f"Link {ref_id}:", value=reference)
        fields.append(field)

    description = f"There were {member_reference.count} entries found for user: **{member_reference.member_name}**\n"
    message = OfferMessage(description, fields)

    return message

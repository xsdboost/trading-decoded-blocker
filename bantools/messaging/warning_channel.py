from typing import List

from bantools.use_cases.listeners import MemberReferenceCount


def append_reference_links(reference_urls: List[str]) -> str:

    """
    Parameters
    ----------
    reference_urls: List[str]
        list of jump urls

    Returns
    -------
    str
       a flattened list of link references to channel jump urls discord text encoded

    Raises
    ------


    """

    links: List[str] = list()

    for entry_id, reference_url in enumerate(reference_urls):
        links.append(f"[reference {entry_id}]({reference_url})\n")

    return "".join(links)


def offender_found(member_reference: MemberReferenceCount) -> str:
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
    message_content: str = (
        f"""Member: {member_reference.member_name} was found to have {member_reference.count} entries\n"""
        + append_reference_links(member_reference.references)
    )

    return message_content

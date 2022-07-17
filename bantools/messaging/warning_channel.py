from typing import List
from bantools.use_cases.listeners import MemberReferenceCount


def append_reference_links(reference_urls: List[str]) -> str:

    links: List[str] = list()
    for entry_id, reference_url in enumerate(reference_urls):
        links.append(f"[reference {entry_id}]({reference_url})\n")

    return "".join(links)


def offender_found(member_refence: MemberReferenceCount) -> str:
    message_content: str = (
        f"""Member: {member_refence.member_name} was found to have {member_refence.count} entries\n"""
        + append_reference_links(member_refence.references)
    )

    return message_content

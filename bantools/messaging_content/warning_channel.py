from typing import List
from discord import Embed, Color

from bantools.use_cases.listeners import MemberReferenceCount


def offender_found(member_reference: MemberReferenceCount) -> Embed:
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

    embed = Embed(
        title=f"Possible duplicate signups found",
        color=Color.red(),
        description=f"""There were {member_reference.count} entries found for user: **{member_reference.member_name}**\n""",
    )
    for ref_id, reference in enumerate(member_reference.references, start=1):
        embed.add_field(name=f"Reference {ref_id}:", value=reference, inline=False)

    return embed

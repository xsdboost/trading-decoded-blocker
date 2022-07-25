def new_user_logger_parser_rule_001(message_text: str) -> str:
    """
    Contains rules for parsing member name from discord message

    Important: This method should be the only member name parser of the project any need for parsing should refer heres

    Parameters
    ----------
    message_text: str
        Full discord message text

    Returns
    -------
    str
        Member name parse from message text
    """

    """
    Note: The current parsing rule is simply break on spaces and get the first entry
    this will get much more complicated once we get projects real data
    """

    return message_text.split()[0]


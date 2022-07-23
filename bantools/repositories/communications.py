from discord import utils, Guild, TextChannel
from bantools.messaging_content.warning_channel import OfferMessage


class ChannelCommunicator:
    def __init__(self, guild: Guild, channel_name: str):
        self.guild: Guild = guild
        self.channel: TextChannel = self._get_channel_by_name(channel_name)

    def _get_channel_by_name(self, channel_name: str) -> TextChannel:
        """
        Given a channel name retrieves the accompanying TextChannel object

        Parameters
        ----------
        channel_name: str
            The channel we want to retrieve the Textchannel object for
        Returns
        -------
        TextChannel
            channel in guild that has channel name

        """
        return utils.get(self.guild.channels, name=channel_name)

    async def send(self, offend_message: OfferMessage) -> None:
        """

        Method send Text embed objects to discord server

        Parameters
        ----------
        offend_message: OfferMessage
            Embed object to be send by TextChannel

        Returns
        -------
        None

        """
        await self.channel.send(embed=offend_message.content)

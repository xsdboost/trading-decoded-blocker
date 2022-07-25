from discord import utils, Guild, TextChannel, Embed, Color
from bantools.messaging.warning_text import OfferMessage


class ChannelCommunicator:
    def __init__(self, guild: Guild, channel_name: str) -> None:
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
        embed = Embed(
            color=0x5EEEAE,
            description=offend_message.description,
            title="Duplicate 7-day trial entries"
        )

        for field in offend_message.reference_links:
            embed.add_field(name=field.name, value=field.value, inline=False)

        await self.channel.send(embed=embed)

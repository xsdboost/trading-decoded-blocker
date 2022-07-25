from discord import utils, Guild, TextChannel, Embed, Color
from bantools.messaging.warning_text import OfferMessage


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
        embed = Embed(
            color=Color.red(),
            description=offend_message.description,
        )

        embed.set_author(name="Duplicate 7-day trial entries")
        embed.set_image(
            url="https://media3.giphy.com/media/wYyTHMm50f4Dm/giphy.gif?cid=ecf05e47yz5qxgjlg0snlf5jr3si98xaond8zub8zoj4oaj8&rid=giphy.gif"
        )

        for field in offend_message.reference_links:
            embed.add_field(name=field.name, value=field.value, inline=False)

        await self.channel.send(embed=embed)

from discord import utils, Guild, TextChannel
from bantools.messaging_content.warning_channel import OfferMessage

class ChannelCommunicator:
    def __init__(self, guild: Guild, channel_name: str):
        self.guild: Guild = guild
        self.channel: TextChannel = self._get_channel_by_name(channel_name)

    def _get_channel_by_name(self, channel_name: str):
        return utils.get(self.guild.channels, name=channel_name)

    @property
    def channel_name(self):
        return self.channel.name

    @channel_name.setter
    def channel_name(self, channel_name: str):
        self.channel = self._get_channel_by_name(channel_name)

    async def send(self, offend_message: OfferMessage):
        await self.channel.send(embed=offend_message.content)

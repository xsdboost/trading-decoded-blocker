from discord import utils, Guild, TextChannel


class ChannelCommunicator:
    def __init__(self, guild: Guild, channel_name: str):
        self.guild: Guild = guild
        self.channel: TextChannel = self._get_channel_by_name(channel_name)

    def _get_channel_by_name(self, channel_name: str):
        channel_id: int = utils.get(self.guild.channels, name=channel_name)
        return self.guild.get_channel(channel_id)

    @property
    def channel_name(self):
        return self.channel.name

    @channel_name.setter
    def channel_name(self, channel_name: str):
        self.channel = self._get_channel_by_name(channel_name)

    def send(self, message: str):
        self.channel.send(content=message)

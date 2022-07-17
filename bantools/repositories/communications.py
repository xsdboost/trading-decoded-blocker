from discord.ext.commands import Bot


class ChannelCommunicator:
    def __init__(self, bot: Bot, channel_name: str):
        self.core_bot = bot
        self.set_channel(channel_name)

    def set_channel(self, channel_name: str):
        pass

    @property
    def channel_name(self):
        return self.discord_channel_name

    @channel_name.setter
    def set_channel_name(self, channel_name: str):
        self.set_channel(channel_name)

    def send(self, message: str):
        pass

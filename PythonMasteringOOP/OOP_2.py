from random import choice
"""A Television and Remote Control Class"""
"""Operates the Television Class via Remote Control Class"""


class Television:
    def __init__(self):
        """The Television Configurations"""
        self.isOn = 'OFF'
        self.isMuted = 'OFF'
        self.volume = 10    # Total max volume is 20
        self.channels = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.current_channel = 7


class RemoteControl(Television):
    count = 0

    def __init__(self):
        RemoteControl.count += 1
        super().__init__()

    def turn_on_tv(self):
        self.isOn = 'ON'

    def turn_off_tv(self):
        self.isOn = 'OFF'

    # Remote Control Commands as Class Methods
    def volume_up(self):
        if self.isOn == 'ON':
            if self.volume < 20:
                self.isMuted = 'OFF'
                self.volume += 1

    def volume_down(self):
        if self.isOn == 'ON':
            if self.volume > 0:
                self.isMuted = 'OFF'
                self.volume -= 1

    def channel_nav_up(self):
        if self.isOn == 'ON':
            for i, ele in enumerate(self.channels):
                if ele == self.current_channel:
                    self.current_channel = self.channels[i+1]
                    break

    def channel_nav_down(self):
        if self.isOn == 'ON':
            for i, ele in enumerate(self.channels):
                if ele == self.current_channel:
                    self.current_channel = self.channels[i-1]
                    break

    def mute(self):
        if self.isOn == 'ON':
            self.isMuted = 'ON'

    def randomize_channel(self):
        if self.isOn == 'ON':
            self.current_channel = choice(self.channels)

    def show_channels(self):
        if self.isOn == 'ON':
            print('Channels available are: ')
            for i, ele in enumerate(self.channels):
                print(f'{ele}', end=' ')

    def input_channel_number(self, channel_input):
        if self.isOn == 'ON':
            if channel_input in self.channels:
                self.current_channel = channel_input

    def get_info(self):
        print(f'TV STATUS for Configuration {RemoteControl.count}: \n'
              f'\tTV is: {self.isOn}\n'
              f'\tCurrent Channel: {self.current_channel}\n'
              f'\tTV Volume: {self.volume}\n'
              f'\tTV is Muted: {self.isMuted}\n')


if __name__ == '__main__':
    user1 = RemoteControl()
    user1.turn_on_tv()
    user1.channel_nav_up()
    user1.channel_nav_up()
    user1.channel_nav_up()
    user1.channel_nav_down()
    user1.input_channel_number(65)
    user1.channel_nav_down()
    user1.randomize_channel()
    user1.get_info()

    user2 = RemoteControl()
    user2.turn_on_tv()
    user2.channel_nav_down()
    user2.channel_nav_down()
    # for i in range(60):
    # user2.volume_up()
    user2.volume_up()

    user2.get_info()


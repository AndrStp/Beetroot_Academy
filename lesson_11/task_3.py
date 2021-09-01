# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# - first_channel() - turns on the first channel from the list.
# - last_channel() - turns on the last channel from the list.
# - turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# - next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# - previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# - current_channel() - returns the name of the current channel.
# - is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", 
# if the channel N or 'name' exists in the list, or "No" - in the other case.

from itertools import cycle, islice


class TV_Controller:
    """TV Controller"""

    def __init__(self, channels: list) -> None:
        self.channels = channels
        self.current = self.channels[0]

    def play(self) -> None:
        """Controls the TV"""
        print('TV Remote controller interface')
        print("""
        - first_channel - turns on the first channel from the list.
        - last_channel - turns on the last channel from the list.
        - turn_channel - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
        - next_channel - turns on the next channel. If the current channel is the last one, turns on the first channel.
        - previous_channel - turns on the previous channel. If the current channel is the first one, turns on the last channel.
        - current_channel - returns the name of the current channel.
        - is_exist - returns "Yes" if the channel N or 'name' exists in the list, or "No" - in the other case.
        - off - swith off the TV and exit the program.
        """)

        while True:
            _commands = ['first_channel', 'last_channel', 'turn_channel', 'next_channel', 'previous_channel', 'current_channel', 'is_exist', 'off']
            command = input('Enter you command: ')
            while command not in _commands: 
                print(f'No such command "{command}", try again\n')
                command = input('Enter you command: ') 

            if command == 'off':
                print('Switching off the TV...')
                quit()
                
            method_to_call = getattr(self, command)
            if command == 'is_exist':
                user_channel = input('Enter the channel name or number here: ')
                result = method_to_call(user_channel)
            elif command == 'turn_channel':
                user_channel = int(input('Enter the channel number here: '))
                result = method_to_call(user_channel)
            else:
                result = method_to_call()
            
            print(result)
            print()
    
    def first_channel(self) -> str:
        self.current = self.channels[0]
        return self.current
    
    def last_channel(self) -> str:
        self.current = self.channels[-1]
        return self.current
    
    def turn_channel(self, channel: int) -> str:
        if self.is_exist(channel) == 'Yes':
            self.current = self.channels[channel]
            return self.current
        else:
            return f'No such channel'

    def next_channel(self) -> str:
        ### solve using itertools cycle and islice ###
        # channels = cycle(self.channels)
        # start = islice(channels, self.channels.index(self.current) + 1, None)
        # self.current = next(start)

        ### solve using iter() ###
        # channels = iter(self.channels[self.channels.index(self.current)+1:])
        # try:
        #     self.current = next(channels)
        # except StopIteration:
        #     channels = iter(self.channels)
        #     self.current = next(channels)

        ### solve using elif and list index ###
        # next_channel_index = self.channels.index(self.current) + 1
        # if next_channel_index > len(self.channels) - 1:
        #     self.current = self.channels[0]
        # else:
        #     self.current = self.channels[next_channel_index]

        ### solve using modulo operator (%) ###
        current_channel_index = self.channels.index(self.current)
        self.current = self.channels[(current_channel_index + 1) % len(self.channels)]

        return self.current
    
    def previous_channel(self) -> str:
        ### solve using itertools cycle and islice ###
        # channels = cycle(reversed(self.channels))
        # start = islice(channels, list(reversed(self.channels)).index(self.current) + 1, None)
        # self.current = next(start)

        ### solve using iter() ###
        # channels = iter(reversed(self.channels[:self.channels.index(self.current)]))
        # try:
        #     self.current = next(channels)
        # except StopIteration:
        #     channels = iter(reversed(self.channels))
        #     self.current = next(channels)

        ### solve using elif and list index ###
        # prev_channel_index = self.channels.index(self.current) - 1
        # if prev_channel_index < 0:
        #     self.current = self.channels[-1]
        # else:
        #     self.current = self.channels[prev_channel_index]

        ### solve using modulo operator (%) ###
        current_channel_index = self.channels.index(self.current)
        self.current = self.channels[(current_channel_index - 1) % len(self.channels)]

        return self.current

    def current_channel(self) -> str:
        return self.current

    def is_exist(self, channel: int or str) -> str:
        if type(channel) == int:
            try:
                self.channels[channel-1]
            except IndexError:
                return 'No'
            else:
                return 'Yes'
        else:
            if channel in self.channels:
                return 'Yes'


CHANNELS = ["BBC", "Discovery", "TV1000"]

tv = TV_Controller(CHANNELS)
tv.play()
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''initializes television object'''
        self.__status = False # False is off, True is On
        self.__muted = False # False is unmuted, True is muted
        self.__volume = Television.MIN_VOLUME   #
        self.__channel = Television.MIN_CHANNEL  

    def power(self) -> None:
        '''switches boolean value'''
        if self.__status == False:
            self.__status = True

        elif self.__status == True:
            self.__status = False

    #
    def mute(self) -> None:
        '''checks to see if power is on and if it is,
        it switches the mute from on and off'''
         if self.__status == True:
            
            # if unmuted, then mute
            if self.__muted == False:
                self.__muted = True
            #if muted, then ummute
            elif self.__muted == True:
                self.__muted = False

    def channel_up(self) -> None:
        '''checks if power is on and if it is, it will make the channel go up to max
        and if it is max it sets is back to the first channel'''
        if self.__status == True:
            
            #if channel is less than the max, then go up a channel
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            #if channel is max channel, then goes to minimum channel
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''Checks if the power is on and if the power is on it 
        makes the channel go down one. If the channel is at the first channel,
        it goes back to the last channel'''
        if self.__status == True:
            #if channel is greater than the min, then go updown a channel
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            #if channel is min channel, then goes to maximum channel
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''Checks if the power is on. If it is on it increments the volume up by one.
        It goes up until the max volume, if it's at the max it doesn't go up anymore'''
        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''Checks if power is on. If it is on the volume goes down until the 
        minimum value then doesn't go down any further'''
        if self.__status == True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
    '''Return the status of the power, channel, and Volume variables'''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume}.'

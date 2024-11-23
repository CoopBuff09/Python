class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False # False is off, True is On
        self.__muted = False # False is unmuted, True is muted
        self.__volume = Television.MIN_VOLUME   #
        self.__channel = Television.MIN_CHANNEL  

    def power(self):
        #print('power')
        if self.__status == False:
            self.__status = True

        elif self.__status == True:
            self.__status = False

    #
    def mute(self):
         #print('mute')
         if self.__status == True:
            
            # if unmuted, then mute
            if self.__muted == False:
                self.__muted = True
            #if muted, then ummute
            elif self.__muted == True:
                self.__muted = False

    def channel_up(self):
        #print('up')
        if self.__status == True:
            
            #if channel is less than the max, then go up a channel
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            #if channel is max channel, then goes to minimum channel
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        #print('down')
        if self.__status == True:
            #if channel is greater than the min, then go updown a channel
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            #if channel is min channel, then goes to maximum channel
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        #print('vol up')
        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        #print('vol down')
        if self.__status == True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume}'

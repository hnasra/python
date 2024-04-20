class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize Television object.
        """
        self.__status: = False  
        self.__muted: = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turning on and off the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the television if it's powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by one if the television is powered on.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by one if the television is powered on.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by one if the television is powered on.
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False

    def volume_down(self) -> None:
        """
        Decrease the volume by one if the television is powered on.
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False

    def __str__(self) -> str:
        """
        Return a string representation of the television's status.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

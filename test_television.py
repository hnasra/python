import pytest
from television import Television
class Test:

    def test_init(self):
        tv = Television()
        assert tv._Television__status == False
        assert tv._Television__muted == False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self):
        tv = Television()
        tv.power()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"
        tv.power()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        tv = Television()
        tv.volume_up()
        tv.mute()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.mute()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        for _ in range(4):
            tv.channel_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        for _ in range(12):
            tv.channel_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        for _ in range(3):
            tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        tv = Television()
        tv.volume_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"



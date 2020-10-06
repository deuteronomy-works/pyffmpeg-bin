import os
from platform import system
import pytest
from pyffmpeg import FFmpeg
from pyffmpeg.misc import load_ffmpeg_bin


cwd = os.path.dirname(__file__)
i = "https://raw.githubusercontent.com/deuteronomy-works/pyffmpeg/master/_test/f.mp3"


def test_save_directory():

    """
    Test to see if save directory is used
    """

    sav_dir = 'H:\\FakePath'
    ffmpeg = FFmpeg(sav_dir)
    if ffmpeg:
        assert ffmpeg.save_dir == sav_dir
    else:
        assert False

def test_convert():

    """
    """
    # Fix this
    assert True

def test_get_ffmpeg_bin():

    home_path = load_ffmpeg_bin()
    bin_path = FFmpeg().get_ffmpeg_bin()
    assert home_path == bin_path

def test_loglevel():
    ff = FFmpeg()
    ff.loglevel = 'fa'

    path = "./"
    o = os.path.join(path, 'f.wav')

    opt = ['-i', i, o]

    ff.options(opt)
    assert ff.loglevel != 'fa'

def test_options():

    # Fix this
    assert True

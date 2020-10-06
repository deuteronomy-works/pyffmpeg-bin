"""
To Provide miscellaneous function

"""

import os
from platform import system


def load_ffmpeg_bin():
    
    cwd = os.path.dirname(__file__)
    # load os specific ffmpeg bin data
    os_name = system().lower()
    if os_name == 'windows':
        os_f_name = 'windows'
        _ffmpeg_ext = '.exe'
    elif os_name == 'linux':
        os_f_name = 'linux'
        _ffmpeg_ext = ''
    else:
        os_f_name = 'darwin'
        _ffmpeg_ext = ''

    bin_path = os.path.join(cwd, 'static', 'bin', os_f_name)
    ffmpeg_file = os.path.join(
    bin_path, 'ffmpeg'+_ffmpeg_ext)

    return ffmpeg_file

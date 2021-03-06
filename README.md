# pyffmpeg-bin [![Downloads](https://pepy.tech/badge/pyffmpeg-bin)](https://pepy.tech/project/pyffmpeg-bin)

FFmpeg wrapper for python.

Same as pyffmpeg but its unserialised.

This unserialised version means the ffmpeg binary comes with it as a binary and needs
not be built at runtime.

The beautiful thing about it is that it comes with its own FFmpeg executable. It is compressed, making it the smallest you can find. And becuase its cross-platform and python 3, it is the only option available for building cross-platform apps with ffmpeg in python.


## Installation
    pip install pyffmpeg-bin

## Usage
```python
from pyffmpeg import FFmpeg

inp = 'path/to/music_folder/f.mp4'
out = 'path/to/music_folder/f.mp3'

ff = FFmpeg()

output_file = ff.convert(inp, out)

print(output_file)


```

## Advanced Usage
```python
from pyffmpeg import FFmpeg
```

### Use a global directory to store all converted files
```python
ff = FFmpeg('path/to/app_folder')
ff.convert('path/to/music_folder/f.mp3', 'f.wav')
```

### Overwrite (Default is set to True)
```python
ff.overwrite = False # do not overwrite but exit immediately
```

## Wiki
The wiki can be located [here](https://github.com/deuteronomy-works/pyffmpeg/wiki)

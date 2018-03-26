#!usr/bin/env python
# coding=utf-8
import os
import pyaudio
import wave
import threading


# https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/
class Sound(threading.Thread):
    def __init__(self, guid):
        threading.Thread.__init__(self)
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
        # ... Other thread setup code here ...
        self.guid = guid

    def run(self):
        # define stream chunk
        chunk = 1024

        # expression_in_phrase
        fpath = os.path.dirname(__file__) + "/sounds/" + str(self.guid) + ".wav"

        # open a wav format music
        f = wave.open(fpath, "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data and not self.shutdown_flag.is_set():
            stream.write(data)
            data = f.readframes(chunk)

        # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

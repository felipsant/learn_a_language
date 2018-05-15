#!usr/bin/env python
# coding=utf-8
import os
import pyaudio
import wave
import threading
from subprocess import call


# https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/
class Sound(threading.Thread):
    def __init__(self, guid, expression_in_phrase):
        threading.Thread.__init__(self)
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
        # ... Other thread setup code here ...
        self.guid = guid
        self.expression_in_phrase = expression_in_phrase
        self.fpath = os.path.dirname(__file__) + "/sounds/" + str(self.guid)
        self.fpath += ".wav"

    def play_audio_from_file(self):
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(self.fpath, "rb")
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

    def get_audio_from_google(self):
        command = "curl " + \
                "https://translate.google.com/translate_tts?ie=UTF-8&q='" + \
                self.expression_in_phrase + \
                "-H 'Referer: http://translate.google.com/'" + \
                "-H 'User-Agent: stagefright/1.2 (Linux;Android 5.0)'" + \
                "> " + self.path
        call(command)

    def run(self):
        # expression_in_phrase
        if not os.path.exists(self.fpath):
            self.get_audio_from_google()
        self.play_audio_from_file()

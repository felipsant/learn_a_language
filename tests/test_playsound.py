from app.playsound import Sound
from app.app import read_language
import pytest
import json
import time
import os


RUN_PARAMETERS = [("ars_brl", "6ab6ca35485249bd98bc879f66bc7bec",
                   "959e0934f1c74b85a02a2bbaba1a25f9")]


def check_sound_is_playing(expected):
    command = """if grep -q RUNNING /proc/asound/card*/*p/*/status 2>&1; then
        echo True
    else
        echo False
    fi"""
    result = os.popen(command).read().replace('\n', '')
    result = result == 'True'
    assert result == expected


def check_sound(output_json, guid):
    # Filter python objects with list comprehensions
    for x in output_json:
        if x['guid'] == guid:
            output_json = json.loads(json.dumps(x))
            break
    # Transform python object back into json
    print("FILTERED_GUID_JSON:" + str(output_json))
    check_sound_is_playing(False)
    thread_sound = Sound(guid, output_json["expression_in_phrase"][0])
    thread_sound.start()
    time.sleep(3)
    check_sound_is_playing(True)
    thread_sound.shutdown_flag.set()


@pytest.mark.parametrize("language,guid,guid_no_sound", RUN_PARAMETERS)
def test_run(language, guid, guid_no_sound):
    output_json = read_language(language)
    check_sound(output_json, guid)
    check_sound(output_json, guid_no_sound)

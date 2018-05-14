from app.playsound import Sound
from app.app import read_language
import pytest
import json


RUN_PARAMETERS = [("ars_brl", "6ab6ca35485249bd98bc879f66bc7bec")]


@pytest.mark.parametrize("language,guid", RUN_PARAMETERS)
def test_run(language, guid):
    output_json = read_language(language)
    # Filter python objects with list comprehensions
    for x in output_json:
        if x['guid'] == guid:
            output_json = json.loads(json.dumps(x))
            break
    # Transform python object back into json
    print("FILTERED_GUID_JSON:" + str(output_json))
    Sound(guid, output_json["expression_in_phrase"][0]).run('1', debug=True)
    assert 1 == 4

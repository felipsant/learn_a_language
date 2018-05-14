from app.app import read_language, check_size_answer
from app.app import remove_expression_in_phrase, ask_questions
import json
import pytest


RUN_PARAMETERS = [("ars_brl", "6ab6ca35485249bd98bc879f66bc7bec")]


def read_language_unittest(language):
    json_class = read_language(language)
    print("json_class_len: " + str(len(json_class)))
    assert len(json_class) > 4
    return json_class


def check_size_answer_unittest(user_exp, expression, expected):
    result = check_size_answer(user_exp, expression)
    print("check_size_answer: " + str(result))
    assert result == expected


def remove_expression_in_phrase_unittest(expression, phrase, expected):
    result = remove_expression_in_phrase(expression, phrase)
    print(result)
    assert expected in result


def check_ask_questions_unittest(guid, expression, expected):
    result = ask_questions(guid)
    # TODO: Insert the to the ask_question.  expression
    assert expected in result


@pytest.mark.parametrize("language,guid", RUN_PARAMETERS)
def test_functionality(language, guid):
    # Let's read a language
    json_class = read_language_unittest(language)

    # Filter python objects with list comprehensions
    json_records = [x for x in json_class if x['guid'] == guid]
    # Transform python object back into json
    output_json = json.dumps(json_records)
    jsonclass = json.loads(str(output_json))[0]
    print("FILTERED_GUID_JSON:" + str(jsonclass))

    # Run check_size_answer_unittest
    check_size_answer_unittest(jsonclass["expression"],
                               jsonclass["expression"], True)
    check_size_answer_unittest(jsonclass["expression"],
                               "", False)
    remove_expression_in_phrase_unittest(jsonclass["expression"],
                                         jsonclass["expression_in_phrase"][0],
                                         "_" * len(jsonclass["expression"]))

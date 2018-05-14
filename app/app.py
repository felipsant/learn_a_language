# -*- coding: utf-8 -*-
import os
import json
import codecs
import re
from time import sleep
from playsound import Sound


def read_language(language):
    fpath = os.path.dirname(__file__) + "/jsons/" + \
            language + ".json"

    f = codecs.open(fpath, encoding='utf-8', errors='strict')
    json_class = json.load(f)
    f.close()
    return json_class


def check_size_answer(user_exp, expression):
    if len(user_exp) != len(expression):
        print("Size Answer vs Expression: " + str(len(user_exp)) + "/" +
              str(len(expression)))
        return False
    return True


def remove_expression_in_phrase(expression, expression_phrase):
    insensitive_hippo = re.compile(re.escape(expression),
                                   re.IGNORECASE)
    exp = insensitive_hippo.sub("_" * len(expression), expression_phrase)
    return exp


def ask_questions(json_class, level):
    size = len(json_class)
    for i in xrange(size):
        if level == 0:
            item = json_class[(size+1) - i]
        else:
            item = json_class[i]

        expression = item["expression"]
        print("Expression: " + expression)

        expression_brl = item["expression_brl"]
        print("Translated: " + expression_brl)

        expression_phrase = item["expression_in_phrase"]
        for x in xrange(len(expression_phrase)):
            phrase = remove_expression_in_phrase(expression,
                                                 expression_phrase[x])
            print("Phrase: " + phrase)

            user_exp = raw_input("Type the Expression: ").decode('utf-8')
            while user_exp != expression:
                check_size_answer(user_exp, expression)
                user_exp = raw_input("Wrong ReType the Expression: "
                                     ).decode('utf-8')

            while user_exp != "Y" and user_exp != "n":
                user_exp = raw_input("Listen to Audio(Y/n)? "
                                     ).decode('utf-8')

            if(user_exp == "Y"):
                thread_sound = Sound(item["guid"],
                                     item["expression_in_phrase"])
                thread_sound.start()
                while user_exp != "c":
                    user_exp = raw_input("\nPress c to continue \n\n"
                                         ).decode('utf-8')
                thread_sound.shutdown_flag.set()

            print("!!Congratulations!!")
            sleep(0.7)
            os.system("clear")


def run(level=0, language="ars_brl", debug=None):
    json_class = read_language(language)
    ask_questions(json_class, level)

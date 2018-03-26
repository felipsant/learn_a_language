# -*- coding: utf-8 -*-
import os
import json
import codecs
import re
from time import sleep
from playsound import Sound


def readJson(language, level):
        fpath = os.path.dirname(__file__) + "/jsons/" + \
                language + ".json"

        f = codecs.open(fpath, encoding='utf-8', errors='strict')
        json_class = json.load(f)
        f.close()
        return json_class


def checkSizeAnswer(user_exp, expression_origin):
    if len(user_exp) != len(expression_origin):
        print("Size Answer vs Expression: " + str(len(user_exp)) + "/" +
              str(len(expression_origin)))


def askQuestionsJson(json_class_origin, json_class_destiny):
        for i in xrange(len(json_class_origin)):
            item_origin = json_class_origin[i]

            expression_origin = item_origin["expression"]
            expression_phrase_origin = item_origin["expression_in_phrase"]

            item_destiny = json_class_destiny[i]
            expression_destiny = item_destiny["expression"]

            for x in xrange(len(expression_phrase_origin)):
                le_phrase_origin = expression_phrase_origin[x]
                insensitive_hippo = re.compile(re.escape(expression_origin),
                                               re.IGNORECASE)
                exp = insensitive_hippo.sub("_" * len(expression_origin),
                                            le_phrase_origin)

                print("Expression: " + expression_origin)
                print("Translated: " + expression_destiny)
                print("Phrase: " + exp)

                user_exp = raw_input("Type the Expression: ").decode('utf-8')
                while user_exp != expression_origin:
                    checkSizeAnswer(user_exp, expression_origin)
                    user_exp = raw_input("Wrong ReType the Expression: "
                                         ).decode('utf-8')

                while user_exp != "Y" and user_exp != "n":
                    user_exp = raw_input("Listen to Audio(Y/n)? "
                                         ).decode('utf-8')

                if(user_exp == "Y"):
                    thread_sound = Sound(item_origin["guid"])
                    thread_sound.start()
                    while user_exp != "c":
                        user_exp = raw_input("\nPress c to continue \n\n").decode('utf-8')
                    thread_sound.shutdown_flag.set()

                print("!!Congratulations!!")
                sleep(0.7)
                os.system("clear")


def processJson(level=1, origin="ars", destiny="brl"):
        json_class_origin = readJson(origin, level)
        json_class_destiny = readJson(destiny, level)
        askQuestionsJson(json_class_origin, json_class_destiny)


def run(parameter, debug=None):
    processJson(parameter)

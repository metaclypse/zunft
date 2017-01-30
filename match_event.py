#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class MatchEvent:
    def __init__(self):
        self.message_text = ""
        self.message_caption = ""
        self.message_icon = None

    def __str__(self):
        return "Message Caption: " + self.message_caption + os.linesep + "Message Text:" + self.message_text

    @staticmethod
    def load_event(name, parsedata=""):
        texts_file = "./res/texts.json"
        json_data = open(texts_file).read()
        data = json.loads(json_data)
        texts = data[name]

        event = MatchEvent()
        event.message_caption = texts["title"]
        event.message_text = texts["content"]

        return event

if __name__ == "__main__":
    # buh = MatchEvent.load_event("peace_offer_after_feud")
    # print(buh)
    pass

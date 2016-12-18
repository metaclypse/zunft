#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RecourceManager:
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if RecourceManager.instance is None:
            RecourceManager.instance = RecourceManager()

        return RecourceManager.instance

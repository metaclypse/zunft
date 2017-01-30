#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class ResourceManager:
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if ResourceManager.instance is None:
            ResourceManager.instance = ResourceManager()

        return ResourceManager.instance

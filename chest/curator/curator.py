# -*- coding: utf-8 -*-

import requests

class Curator(object):

    stream_url = "http://curator.im/api/stream/"

    def __init__(self, robot, token):
        self.robot = robot
        self.token = token

    def stream(self, page=1):
        response = requests.get(self.stream_url, params={
            'token': self.token,
            'page' : page
        });

        return response.json()

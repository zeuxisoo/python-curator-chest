# -*- coding: utf-8 -*-

import logging
from curator import Curator
from fetcher import Ranch

class Robot(object):

    def __init__(self, token):
        self.set_token(token)
        self.get_logger()

    def set_token(self, token):
        self.token = token

    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger_stream_handler = logging.StreamHandler()
        logger_stream_handler.setLevel(logging.DEBUG)
        logger_stream_handler.setFormatter(logger_formatter)
        logger.addHandler(logger_stream_handler)

        self.logger = logger

    def start(self, woker_number=2):
        curator = Curator(self, self.token)

        ranch = Ranch(self, curator)
        ranch.start_worker(woker_number)
        ranch.work()


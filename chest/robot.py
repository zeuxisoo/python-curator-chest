# -*- coding: utf-8 -*-

import os
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

    def worker(self, worker):
        self.worker = worker

    def output(self, output):
        self.output = os.path.realpath(output)

    def pageno(self, pageno):
        self.pageno = pageno

    def all_next_page(self, all_next_page):
        self.all_next_page = all_next_page

    def start(self):
        self.logger.debug("Worker     : {0}".format(self.worker))
        self.logger.debug("Output     : {0}".format(self.output))
        self.logger.debug("PageNo     : {0}".format(self.pageno))
        self.logger.debug("AllNextPage: {0}".format(self.all_next_page))

        curator = Curator(self, self.token)

        ranch = Ranch(self, curator)
        ranch.worker(self.worker)
        ranch.output(self.output)
        ranch.start_worker()
        ranch.work(
            page=self.pageno,
            all_next_page=self.all_next_page
        )


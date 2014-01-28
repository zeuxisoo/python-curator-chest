# -*- coding: utf-8 -*-

from Queue import Queue
from .worker import StreamWorker

class Ranch(object):

    stream_result_queue = Queue()

    def __init__(self, robot, curator, out_directory):
        self.robot         = robot
        self.curator       = curator
        self.out_directory = out_directory

    def work(self, page=1):
        stream = self.curator.stream(page=page)

        for result in stream['results']:
            self.stream_result_queue.put(result)

        # if stream['next']:
        #     self.download(page + 1)
        # else:
        #     self.stram_result_queue.join()

        self.stream_result_queue.join()

    def start_worker(self, number_):
        for no in range(number_):
            worker = StreamWorker(self.robot, no, self.stream_result_queue, self.out_directory)
            worker.setDaemon(True)
            worker.start()

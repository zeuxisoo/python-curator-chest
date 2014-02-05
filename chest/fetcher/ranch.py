# -*- coding: utf-8 -*-

from Queue import Queue
from .worker import StreamWorker
from .watcher import Watcher

class Ranch(object):

    stream_result_queue = Queue()

    def __init__(self, robot, curator):
        self.robot         = robot
        self.curator       = curator

    def worker(self, worker):
        self.worker = worker

    def output(self, output):
        self.output = output

    def start_worker(self):
        Watcher()
        for no in range(self.worker):
            worker = StreamWorker(self.robot, no, self.stream_result_queue)
            worker.output(self.output)
            worker.setDaemon(True)
            worker.start()

            self.robot.logger.debug("WorkerNo ==> {0} ==> Started".format(no))

    def work(self, page=1, all_next_page=False):
        stream = self.curator.stream(page=page)

        for result in stream['results']:
            self.robot.logger.debug("Queueing ==> {0} ==> {1}".format(result['id'], result['name'].encode("UTF-8")))

            self.stream_result_queue.put(result)

        if stream['next'] and all_next_page:
            next_page = page + 1

            self.robot.logger.debug("Paginate ==> {0}".format(next_page))
            self.work(next_page)
        else:
            self.robot.logger.debug("Queueing ==> calling join")
            self.stream_result_queue.join()

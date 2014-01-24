# -*- coding: utf-8 -*-

from threading import Thread

class StreamWorker(Thread):

    def __init__(self, robot, no, queue):
        Thread.__init__(self)

        self.robot = robot
        self.no    = no
        self.queue = queue

    def run(self):
        while True:
            stream_result = self.queue.get()

            self.robot.logger.debug("{0} {1}".format(self.no, stream_result['id']))

            self.queue.task_done()

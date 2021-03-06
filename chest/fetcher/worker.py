# -*- coding: utf-8 -*-

import os
import errno
import requests
from threading import Thread

class StreamWorker(Thread):

    def __init__(self, robot, no, queue):
        Thread.__init__(self)

        self.robot = robot
        self.no    = no
        self.queue = queue

    def output(self, output):
        self.output = output

    def run(self):
        while True:
            stream_result = self.queue.get()

            extension  = os.path.splitext(stream_result['image'])[1]
            save_path  = "{0}/{1}{2}".format(self.output, stream_result['id'], extension)

            self.mkdir(self.output)
            self.save(save_path, stream_result)
            self.queue.task_done()

    def mkdir(self, directory):
        try:
            os.mkdir(directory)
        except OSError as err:
            if err.errno == errno.EEXIST and os.path.isdir(directory):
                pass

    def save(self, save_path, stream_reuslt):
        result_id    = stream_reuslt['id']
        result_name  = stream_reuslt['name'].encode("UTF-8")
        result_src   = stream_reuslt['image']

        debug_string = '{0:<8} ==> {1} ==> {2}'

        r = requests.get(result_src, stream=True)

        if r.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)

            self.robot.logger.debug(debug_string.format('Saving..', result_id, result_name))
        else:
            self.robot.logger.debug(debug_string.format('Failed..', result_id, result_name))

# -*- coding: utf-8 -*-

import os
import requests
from threading import Thread

class StreamWorker(Thread):

    def __init__(self, robot, no, queue, out_directory):
        Thread.__init__(self)

        self.robot         = robot
        self.no            = no
        self.queue         = queue
        self.out_directory = out_directory

    def run(self):
        while True:
            stream_result = self.queue.get()

            image_src = stream_result['image']
            extension  = os.path.splitext(image_src)[1]
            save_path  = "{0}/{1}{2}".format(self.out_directory, stream_result['id'], extension)

            self.mkdir(self.out_directory)
            self.save(save_path, image_src)
            self.queue.task_done()

    def mkdir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save(self, save_path, src):
        r = requests.get(src, stream=True)

        if r.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)



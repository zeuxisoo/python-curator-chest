#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
from chest import robot

if __name__ == "__main__":
    parser = optparse.OptionParser(usage="Usage: %prog -t [TOKEN]")

    parser.add_option("-t", "--token", action="store", dest="token", help="Token for request curator api")
    parser.add_option("-w", "--worker", action="store", dest="worker", default=2, type="int", help="Worker number, default is 2")
    parser.add_option("-o", "--output", action="store", dest="output", default="output", help="Output directory, default is output")

    (options, args) = parser.parse_args()

    if options.token:
        robot = robot.Robot(options.token)
        robot.worker(options.worker)
        robot.output(options.output)
        robot.start()
    else:
        parser.print_help()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
from chest import robot

if __name__ == "__main__":
    parser = optparse.OptionParser(usage="Usage: %prog -t [TOKEN]")

    parser.add_option("-t", "--token", action="store", dest="token", help="Token for request curator api")

    (options, args) = parser.parse_args()

    if options.token:
        robot = robot.Robot(options.token)
        robot.start()
    else:
        parser.print_help()

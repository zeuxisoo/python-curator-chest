#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
from chest import robot

if __name__ == "__main__":
    parser = optparse.OptionParser(usage="Usage: %prog -t [TOKEN]")

    parser.add_option("-t", "--token", action="store", dest="token", help="Token for request curator api")
    parser.add_option("-w", "--worker", action="store", dest="worker", default=2, type="int", help="Worker number, default is 2")
    parser.add_option("-o", "--output", action="store", dest="output", default="output", help="Output directory, default is output")
    parser.add_option("-p", "--pageno", action="store", dest="pageno", default=1, type="int", help="Specified page number, default is 1")

    parser.add_option("--all-next-page", action="store_true", dest="all_next_page", help="Fetch all next page, default is True")

    (options, args) = parser.parse_args()

    if options.token:
        robot = robot.Robot(options.token)
        robot.worker(options.worker)
        robot.output(options.output)
        robot.pageno(options.pageno)
        robot.all_next_page(options.all_next_page)
        robot.start()
    else:
        parser.print_help()

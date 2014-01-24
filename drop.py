#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chest import robot
from config import CURATOR_TOKEN

if __name__ == "__main__":
    robot = robot.Robot(CURATOR_TOKEN)
    robot.start()

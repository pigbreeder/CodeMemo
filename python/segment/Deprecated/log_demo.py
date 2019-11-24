#!/usr/bin/env python
# encoding: utf-8
# https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
import logging
import Colors
logging.basicConfig(
        level=logging.DEBUG,
        #filename="test.log", # if write msg to file, remove Colors module to avoid color sep interference
        format="%(asctime)s:%(levelname)s:%(message)s")

logging.debug("Made {} {} pizza(s)".format('quantity', 'name'))
logging.info("some info")
logging.warn("a warning")
logging.error("some error")

"""Logging module for sentinel"""
import logging
import sys


def set_logging(level=None):
    """Set a logger STDOUT"""
    logger = logging.getLogger('STDOUT')
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(out_hdlr)
    logger.setLevel(logging.getLevelName(level))

    return logger

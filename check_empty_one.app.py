# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


reverse = False


def on_set(key, val):
    if key == "reverse":
        global reverse
        reverse = val


def on_get(key):
    if key == "reverse":
        return reverse


def on_run(data):

    # sys.stdout.write(f"[check_empty] condition: {condition}\n")
    # sys.stdout.write(f"[check_empty] condition type: {type(condition)}\n")
    # sys.stdout.write(f"[check_empty] data: {data}\n")
    # sys.stdout.flush()

    if isinstance(data, str):
        if data:
            # sys.stdout.write(f"[check_empty] string True\n")
            # sys.stdout.flush()
            return {'result': data}
        else:
            # sys.stdout.write(f"[check_empty] string False\n")
            # sys.stdout.flush()
            return {}
    else:
        # sys.stdout.write(f"[check_empty] condition.shape: {condition.shape}\n")
        # sys.stdout.flush()
        if data.shape:
            # sys.stdout.write(f"[check_empty] numpy True\n")
            # sys.stdout.flush()
            return {'result': data}
        else:
            # sys.stdout.write(f"[check_empty] numpy False\n")
            # sys.stdout.flush()
            return {}


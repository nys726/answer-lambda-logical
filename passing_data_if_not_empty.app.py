# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


block_passing_data = False


def on_set(key, val):
    if key == "block_passing_data":
        global block_passing_data
        block_passing_data = eval(val)


def on_get(key):
    if key == "block_passing_data":
        return str(block_passing_data)


def on_run(check_value, data):
    if not check_value.shape:
        return return_empty_result()

    if check_value.shape[0] == 0:
        return return_empty_result()

    return {'result': data}


def return_empty_result():
    if block_passing_data:
        return {}
    else:
        return {'result': None}


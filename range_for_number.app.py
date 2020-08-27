# -*- coding: utf-8 -*-

import numpy as np
import time
import sys

block_data = True
reverse = False
range_start = 0.0
eable_range_start = True
range_end = 0.0
eable_range_end = True

true_str_list = ['true']


def on_set(key, val):
    if key == "reverse":
        global reverse
        reverse = True if val.lower() in true_str_list else False
    elif key == "block_data":
        global block_data
        block_data = True if val.lower() in true_str_list else False
    elif key == "range_start":
        global range_start
        range_start = float(val)
    elif key == "enable_range_start":
        global enable_range_start
        enable_range_start = True if val.lower() in true_str_list else False
    elif key == "range_end":
        global range_end
        range_end = float(val)
    elif key == "enable_range_end":
        global enable_range_end
        enable_range_end = True if val.lower() in true_str_list else False


def on_get(key):
    if key == "reverse":
        return str(reverse)
    elif key == "block_data":
        return str(block_data)
    elif key == "range_start":
        return str(range_start)
    elif key == "enable_range_start":
        return str(enable_range_start)
    elif key == "range_end":
        return str(range_end)
    elif key == "enable_range_end":
        return str(enable_range_end)


def on_run(number):
    if not number.shape or len(number.shape) != 1 or number.shape[0] != 1:
        return return_negative()

    data = number[0]

    if (not check_range(data) and not reverse) or (check_range(data) and reverse):
        return return_negative()

    return return_positive(data)


def check_range(num):
    if enable_range_start and enable_range_end:
        if range_start <= num <= range_end:
            return True
    elif not enable_range_start and enable_range_end:
        if num <= range_end:
            return True
    elif enable_range_start and not enable_range_end:
        if range_start <= num <= range_end:
            return True
    elif not enable_range_start and not enable_range_end:
        return True
    return False


def return_positive(data):
    return {'result': np.array([data])}


def return_negative():
    if block_data:
        return {}
    else:
        return {'result': None}


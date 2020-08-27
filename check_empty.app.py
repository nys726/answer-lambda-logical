# -*- coding: utf-8 -*-

import numpy as np
import time
import sys

block_data = True
reverse = False

true_str_list = ['true']

def on_set(key, val):
    if key == "reverse":
        global reverse
        reverse = True if val.lower() in true_str_list else False
    elif key == "block_data":
        global block_data
        block_data = True if val.lower() in true_str_list else False


def on_get(key):
    if key == "reverse":
        return str(reverse)
    elif key == "block_data":
        return str(block_data)


def on_run(condition, data):

    # sys.stdout.write(f"[check_empty] condition: {condition}\n")
    # sys.stdout.write(f"[check_empty] condition type: {type(condition)}\n")
    # sys.stdout.write(f"[check_empty] data: {data}\n")
    # sys.stdout.flush()

    # Positive.
    # c: T , r: F
    # c: F , r: T
    if (condition.shape and not reverse) or (not condition.shape and reverse):
        # sys.stdout.write(f"[check_empty] numpy True\n")
        # sys.stdout.flush()
        return return_positive(data)
    # Negative.
    # c: F , r: F
    # c: T , r: T
    else:
        # sys.stdout.write(f"[check_empty] numpy False\n")
        # sys.stdout.flush()
        return return_negative()


def return_positive(data):
    return {'result': data}

def return_negative():
    if block_data:
        return {}
    else:
        return {'result': None}


# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


reverse = False

true_str_list = ['true']


def on_set(key, val):
    if key == "reverse":
        global reverse
        reverse = True if val.lower() in true_str_list else False


def on_get(key):
    if key == "reverse":
        return str(reverse)


def on_run(condition, true_data, false_data):

    # sys.stdout.write(f"[check_empty] condition: {condition}\n")
    # sys.stdout.write(f"[check_empty] condition type: {type(condition)}\n")
    # sys.stdout.write(f"[check_empty] condition.shape: {condition.shape}\n")
    # sys.stdout.flush()

    if condition.shape:
        # sys.stdout.write(f"[check_empty] numpy True\n")
        # sys.stdout.flush()
        return return_result(True, true_data, false_data)
    else:
        # sys.stdout.write(f"[check_empty] numpy False\n")
        # sys.stdout.flush()
        return return_result(False, true_data, false_data)


def return_result(condition, true_data, false_data):
    # sys.stdout.write(f"[check_empty.return_result] condition {condition}\n")
    # sys.stdout.write(f"[check_empty.return_result] true_data {true_data}\n")
    # sys.stdout.write(f"[check_empty.return_result] false_data {false_data}\n")
    # sys.stdout.write(f"[check_empty.return_result] reverse {reverse}\n")
    # sys.stdout.flush()
    if (condition and not reverse) or (not condition and reverse):
        return {'result': true_data}
    else:
        return {'result': false_data}


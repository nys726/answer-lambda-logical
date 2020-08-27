import sys

control_setting = 'Pass'


def on_set(key, val):
    if key == 'control_setting':
        global control_setting
        control_setting = val

def on_get(key):
    if key == 'control_setting':
        return control_setting

def on_run(data):
    if control_setting == 'None':
        return {'result' : None}
    elif control_setting == 'Pass':
        return {'result' : data}
    else:
        return {}

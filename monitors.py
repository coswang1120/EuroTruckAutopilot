from screeninfo import get_monitors
import re


def get():
    monitors = []

    for m in get_monitors():
        x = (str(m))
        monitors.append(re.sub(r'([?!^monitor()])', '', x))

    return monitors


def get_x_offset(monitor):
    return monitor[monitor.find('+') + 1:monitor.rfind('+')]

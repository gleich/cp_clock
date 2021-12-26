from typing import Tuple
from loguru import logger
from datetime import datetime
from time import sleep


def mainloop(display) -> None:
    logger.info("Starting main loop")

    old_ms_loc = (1, 1)
    old_s_loc = (1, 1)
    old_m_loc = (1, 1)
    old_h_loc = (1, 1)
    old_d_loc = (1, 1)

    while True:
        now = datetime.now()

        # Milliseconds
        ms_loc = coordinate_from_percent((now.microsecond * 0.001) / 999, 0)
        if ms_loc != old_ms_loc:
            set_pixel(display, ms_loc, old_ms_loc)
            old_ms_loc = ms_loc

        # Seconds
        s_loc = coordinate_from_percent(now.second / 59, 1)
        if s_loc != old_s_loc:
            set_pixel(display, s_loc, old_s_loc)
            old_s_loc = s_loc

        # Minutes
        m_loc = coordinate_from_percent(now.minute / 59, 2)
        if m_loc != old_m_loc:
            set_pixel(display, m_loc, old_m_loc)
            old_m_loc = m_loc

        # Hours
        h_loc = coordinate_from_percent(now.hour / 23, 3)
        if h_loc != old_h_loc:
            set_pixel(display, h_loc, old_h_loc)
            old_h_loc = h_loc

        # Days
        d_loc = coordinate_from_percent(now.day / 31, 4)
        if d_loc != old_d_loc:
            set_pixel(display, d_loc, old_d_loc)
            old_d_loc = d_loc


def coordinate_from_percent(percent: float, level: int) -> Tuple:
    x = 0
    y = 0
    coordinate_sum = round(percent * 100 / 6.25)
    if coordinate_sum > 8:
        x = 2
        coordinate_sum -= 8
        y = 8 - coordinate_sum
    else:
        x = 1
        y = coordinate_sum - 1
    if y > 7:
        y = 7
    return (x + (3 * level), y)


def set_pixel(display, loc: Tuple, old_loc: Tuple) -> None:
    display.pixel(old_loc[0], old_loc[1], 1)
    if loc[1] == 0:
        display.pixel(loc[0], loc[1], 50)
    else:
        display.pixel(loc[0], loc[1], 10)

from time import sleep
from loguru import logger


def animate_on(display):
    logger.info("Animating display on")
    for x in range(16):
        for y in range(8):
            display.pixel(x, y, 1)
            sleep(0.02)
    sleep(1)
    display.fill(0)
    logger.success("Animated display on")


def setup_levels(display):
    for x in range(16):
        if x in [0, 3, 6, 9, 12, 15]:
            continue
        for y in range(8):
            display.pixel(x, y, 1)

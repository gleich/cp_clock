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

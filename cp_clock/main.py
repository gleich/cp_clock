import loop
from loguru import logger
from adafruit_is31fl3731.charlie_bonnet import CharlieBonnet
import board
import busio
from time import sleep

import start


def main():
    logger.info("Booted up")
    with board.I2C() as i2c:
        display = CharlieBonnet(i2c)
        start.animate_on(display)
        start.setup_levels(display)
        loop.mainloop(display)


if __name__ == "__main__":
    main()

from loguru import logger
from adafruit_is31fl3731.charlie_bonnet import CharlieBonnet
import board
import busio
from time import sleep


def main():
    logger.debug("Hello World!")
    with board.I2C() as i2c:
        display = CharlieBonnet(i2c)
        display.fill(5)

        sleep(10)
        display.fill(0)


if __name__ == "__main__":
    main()

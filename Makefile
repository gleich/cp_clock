PI_NAME="pi@mg01.local"

deploy:
	rsync -ravP --exclude='/.git' . $(PI_NAME):/home/pi/cp_clock/
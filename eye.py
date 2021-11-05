import time
import beepy

try:
    while True:
        time.sleep(35)
        beepy.beep(sound=1)
except KeyboardInterrupt:
    break

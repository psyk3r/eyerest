import time
import beepy

while True:
    try:
        time.sleep(35)
        beepy.beep(sound=1)
    except KeyboardInterrupt:
        break

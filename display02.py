from SimpleCV import Display, Image
import time

display = Display()
Image("logo").save(display)
print "open window..."

while not display.isDone():
    time.sleep(0.1)



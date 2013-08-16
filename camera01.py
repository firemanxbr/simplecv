from SimpleCV import Camera

"""
 Selected camera id 0 /dev/video0 and set resolution 640x480
"""
cam = Camera(0, { "width": 640, "height": 480 })

img = cam.getImage()
img.drawText("I am you camera id 0...", 10, 10)
img.show()

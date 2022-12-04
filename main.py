from phue import Bridge
from rgbxy import Converter

c = Converter()
b = Bridge("192.168.0.232")
b.connect()
data = b.get_api()

lights = data["lights"]
rgb = (255, 255, 0)
b.set_light(7, "xy", c.rgb_to_xy(*rgb))

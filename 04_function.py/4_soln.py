import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area , circum

a , c = circle_stats(2)

print("Area:", a , "Circum:", c)
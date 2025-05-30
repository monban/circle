from bitmap import Bitmap
from point import Point
import renderer_text

b = Bitmap(40, 40, 20, 20)

r = 16
point = Point(r, 0)

def circleDistance(p: Point, r: int):
    return abs(p.x**2+p.y**2-r**2)

def mirrorPoints(p: Point):
    return [
        Point(p.x, p.y),
        Point(-p.x, p.y),
        Point(p.x, -p.y),
        Point(-p.x, -p.y),
        Point(p.y, p.x),
        Point(-p.y, p.x),
        Point(p.y, -p.x),
        Point(-p.y, -p.x),
    ]
    
while point.y < point.x:
    for p in mirrorPoints(point):
        b.set(p)

    p1 = Point(point.x, point.y+1)
    p2 = Point(point.x-1, point.y+1)
    if circleDistance(p1, r) < circleDistance(p2, r):
        point = p1
    else:
        point = p2

renderer_text.blit(b)

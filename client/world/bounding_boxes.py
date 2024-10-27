from math import sqrt

def collide(rect1, rect2, offset=0):
    """Returns if both bounding boxes collide."""
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    for x, y in ((x2, y2), (x2+w2, y2), (x2, y2+h2), (x2+w2, y2+h2)):
        if x1+w1 > x > x1 and y1+h1 > y > y1:
            return True
    return False

def distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
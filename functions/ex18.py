import math
def calDistance (x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
print(calDistance(1,2,3,4))

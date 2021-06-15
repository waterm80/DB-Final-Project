from math import *


def distance(latA, lonA, latB, lonB):
    ra = 6378.140  # 赤道半徑
    rb = 6356.755  # 極半徑 （km）
    flatten = (ra-rb)/ra  # 地球偏率
    rad_lat_A = radians(latA)
    rad_lng_A = radians(lonA)
    rad_lat_B = radians(latB)
    rad_lng_B = radians(lonB)
    pA = atan(rb/ra*tan(rad_lat_A))
    pB = atan(rb/ra*tan(rad_lat_B))
    xx = acos(sin(pA)*sin(pB)+cos(pA)*cos(pB)*cos(rad_lng_A-rad_lng_B))
    c1 = (sin(xx)-xx)*(sin(pA)+sin(pB))**2/cos(xx/2)**2
    c2 = (sin(xx)+xx)*(sin(pA)-sin(pB))**2/sin(xx/2)**2
    dr = flatten/8*(c1-c2)
    distance = ra*(xx+dr)
    return distance

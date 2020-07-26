#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import radians, degrees, sin, cos, asin, acos, sqrt

def calculate_great_circle(lon1,lat1,lon2,lat2):
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    distance = 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))
    #print (distance)
    return distance


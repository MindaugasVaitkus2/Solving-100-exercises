# Please write a function that calculates liquid volume in a sphere using the following formula.... The radius r  is always 10, so consider making it a default parameter.
from __future__ import division
import math

def volume_sphere (h, r = 10):
    volume = ((4 * math.pi * r**3) / 3) - (math.pi *h**2 * (3 * r - h)/3)
    return volume

x = volume_sphere(2)
print x
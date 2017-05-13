# Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230. 

import ephem
jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
au_distance = jupiter.sun_distance
km_distance = au_distance * 149597870.691
print(km_distance)

# http://rhodesmill.org/pyephem/
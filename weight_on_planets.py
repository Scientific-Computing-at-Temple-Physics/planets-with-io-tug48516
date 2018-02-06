# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

#planet of interest: Jupiter
# 100 m above average Radius
# Explorer=60kg
# Jupiter;  69911 km;  1.326 g/cm^3;  gas giant
# m=mass of explorer
import math as ma
V=(4*ma.pi*(69911*1000)**3)/3.
M=1.326*V
G=((6.67*10**-11)*M*60)/((69911000+100)**2)
F=G*60
print (F,G)

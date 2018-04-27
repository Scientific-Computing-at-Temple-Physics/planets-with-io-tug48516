# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)
#need to find the explorer's weight and gravitational acceleration
#data = open("planet_data.dat","r")

# Explorer's mass is m in kg
m = 50
planet = ["Mercury","Venus","Earth","Mars","Ceres","Jupiter","Saturn","Uranus","Neptune","Pluto","Eris","Comet","Proxima","Kepler-37"]
# r is average radius in km
radius = [2439.7,6051.8,6371.0,3389.5,473,69911,58232,25362,24622,1188.3,1163,3.7,8000.0,2176.0]
#Radius is in m
Radius = [i*1000 for i in radius]

density = [5.427,5.243,5.514,3.933,2.161,1.326,0.687,1.27,1.638,1.854,2.52,0.533,3.636,5.560]
#Density in kg/m^3
Density = [i*1000 for i in density]

# we will use random number generator to chose our planet
#n is planet number
import random
n=random.randint(0,13)
#p is randomply selected planet
p = planet [n]

# r is randomly selected planet's radius
r = Radius [n]

# V is volume of selected planet
V =4./3.*ma.pi*r**3

# d is density of randomly selected planet
d = Density [n]

# M is mass of an object, given its density and volume
M = d*V

# G is gravity constant
G = 6.667*(10**(-11))
# Gravity in selected planet
Fg = G*M/(r**2)

# The explorer's weight is W in planet
W = Fg* m
print ("Explorer's weight",W,"Gravitaty in planet",Fg,"Randomly selected Planet",p)
print ("explorer's weight in earth",m*9.8)

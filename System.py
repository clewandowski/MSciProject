# TO DO
# - exceptions to handle lack of path and stuff
# - amplitude sums
# - implement in functions

from itertools import chain # For joing generators
from model import *

# Global parameters

# Event [Time (0 to T), position (0 or 1)]
# Point it must pass through
E = [[3,0],[5,1]]
T = 9

# Obtain all paths ('Starting at zero')
paths = [format(j, '0'+str(T+1)+'b') for j in range(0, pow(2,T))]

# Filter paths
valid_paths = filter_paths(paths, E)

# Identify number of flips
flips = get_flips(valid_paths)

# Find measure
# Don't kill me for the following line, but I like one-liners :D
measure = sum([pow(1j,flips[i]-flips[j]) for i in range(0,len(valid_paths)) for j in range(0,len(valid_paths))]).real/pow(2,T)
    
print "Measure: ", measure
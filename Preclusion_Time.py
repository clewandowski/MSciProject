# TO-DO:
# - consistency with naming
# - given time (and hence length) of a string at which we can preclude an event
#   explicitly determine what cylinders sets must be added to do so

import numpy as np

# The u vector
#u = np.array([ [ 0] , [1]])
u = np.array([ [0], [ 1] ])

# the klmn vector (also called P)
# Order: +1 -1 +i -i
#k = np.array([ [1], [0], [0], [0]])
k = np.array([[1],[1],[1],[0]])

# Definition of matrices
M = np.array([ [1,0,0,1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1]]) # Evolution of klmn vector
U = np.array([ [1, -1], [1, 1]]) # Evolution of the u vector

# Loop conditions
safety = 0 # To prevent infinite loops
not_found = True # Loop condition
# Dummy variables for clarity (could be one if loop :D)
real_part = False
imag_part = False

# Loop
while not_found:
    # Output
    print 'T = ', safety
    print 'P = ', (zip(*k)), ' S = ', zip(*u)

    # Check conditions 
    # Note: Could be one if statement, but broken down for clarity
    # Real component amplitudes
    if ((u[0][0] < 0) and (-1*u[0][0] == k[0][0])) or (u[0][0] > 0) and (u[0][0] == k[1][0]) or (u[0][0] == 0) :
        real_part = True
    
    # Imag component amplitudes
    if ((u[1][0] < 0) and (-1*u[1][0] == k[2][0])) or ((u[1][0] > 0) and (u[1][0] == k[3][0])) or (u[1][0] == 0):
        imag_part = True
    
    # Check if both components can be cancelled    
    if real_part and imag_part:
        print 'Required T = ', safety
        not_found = False
    else: # Set variables back to false
        real_part = False
        imag_part = False
    
    # Iterate infinite loop counter safety measure    
    safety += 1  
    if safety == 10:
        not_found = False
   
    # Propagate k and u vectors from T to T+1 
    k = np.dot(M,k);
    u = np.dot(U,u)


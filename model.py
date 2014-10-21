
# Identify valid paths    
def filter_paths(paths, E):
    ''' Identify, which paths satisfy all event conditions '''
    valid_paths = []
    # Loop over paths
    for p in paths:
        counter = 0
        for e in E:
            if int(p[e[0]]) == e[1]:
                counter += 1
 
        if counter == len(E): # All conditions are met => Change if multiple paths are to be considered
            valid_paths.append(p)
            
    return valid_paths
    
# Get number of swaps in a path
def get_flips(paths):
    ''' Determines number of swaps in a path '''
    flips = [] 
    k = 0;
    
    # Maybe use comprehensions?
    for p in paths:
        flips.append(0)
        for i in range(0,len(p)-1):
            if (int(p[i])+int(p[i+1]))%2 == 1:
                flips[k] += 1
              
        k += 1
        
    return flips
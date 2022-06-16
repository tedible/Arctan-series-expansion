import numpy as np

def arctan(x,n):
    
    """Returns series expansion of arctan(x); n = iterations."""
    
    answer = 0
    
    for i in range (0,n+1):
        
        if -1<=x<0 or 0<x<=1:
            answer += (((-1)**i) / (2*i + 1)) * x ** (2*i +1)
            return answer
        elif x<-1:
            answer += (((-1)**i) / (2*i + 1)) * (1/x) ** (2*i +1)
            return - np.pi/2 - answer
        elif x>1:
            answer += (((-1)**i) / (2*i + 1)) * (1/x) ** (2*i +1)
            return np.pi/2 - answer
        else:
            return 0
            
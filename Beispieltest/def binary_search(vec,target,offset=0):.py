def binary_search(vec,target,offset=0):

    n=len(vec)

    if n == 1 and vec[0] == target:
        return 0
    
    elif n==1 and vec[0] != target:
        return -1
        
    elif n == 0:
        return -1
    
    mid_val=vec[n//2]
    
    if mid_val == target: 
        return offset + n//2
        
    elif target<mid_val:
        return binary_search(vec[:n//2],target,offset)
        
    else:
        return binary_search(vec[(n//2)+1:],target, offset+(n//2)+1)



        



def solution(A):
    """
    If input array is empty return -1
    else return top of sorted all places
    """
    if not A:
        return -1
        
    unique_palces = list(set(A))
    last_palces = []
    for index, p in  enumerate(A):
        try:
            possible_plan = [ A.index(place, index) for place in unique_palces]
            last_palces.append(max(possible_plan)- min(possible_plan)+1)
        except:
            pass
    if last_palces:  
        print last_palces
        last_palces.sort()
        return last_palces[0]
    else:
        return -1


A =   [7, 3, 7, 3, 1, 3, 4, 1] 
print solution(A)
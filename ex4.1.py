"""
1.  
    Best Case: All elements are less than or equal to 5. O(n)
    
    Worst Case: All elenents are greater than 5. O(n^2)
    
    Average Case: Elements are random. O(n^2)

2.
    In the code below, all of the case complexities are the same (O(n)):
"""
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
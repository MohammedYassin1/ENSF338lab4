"""
1.  
    Best Case: All elements are less than or equal to 5. In this case the inner loop is never triggered, .....
    
    Worst Case: All elenents are greater than 5. In this case the inner loop is always triggered, ...
    
    Average Case: Elements are random. This causes the inner loop to trigger .....

2.
    In the code below, all of the case complexities are the same (O(n)):
"""
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
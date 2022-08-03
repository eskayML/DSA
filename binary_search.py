#binary search

def binary_search(arr,val):
    high = len(arr) -1 
    low = 0
    
    while high >= low :
        mid = (high+low)//2
        if arr[mid] > val:
            high = mid
        elif arr[mid] < val:
            low = mid
        else:
            return mid
    
    return -1
    #if the element is absent


test = [1,3,5,7,9]
print(binary_search(test,2))
        
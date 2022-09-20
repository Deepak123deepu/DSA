def binarySearch(list,startIndex, endIndex, n):
    # mid = int(len(list)/2)
    # if n == list[mid]:
    #     return f'found element at {mid}'
    # elif n > list[mid]:
    #     temp = list[mid:]
    #     mid1 = int(len(temp)/2)
    #     if mid1 == n:
    #         return f'found element at {mid1}'
    #      else: 
    #         .
    #         .
    #         .
    # return list[mid]
    
    while startIndex <= endIndex:
        
        mid = startIndex + (endIndex - startIndex) // 2 
        
        if list[mid] == n:
            return mid
        elif n>list[mid]:
            startIndex = mid + 1 
        else:
            endIndex = mid - 1 
        
    return -1 
    
list = [1,2,3,5,6]
# print(list[2:])
# print(binarySearch(sorted(list), 0, len(list)-1, 5))
print(f'the element is found at index {binarySearch(sorted(list), 0, len(list)-1, 5)} and the value is {list[binarySearch(sorted(list), 0, len(list)-1, 5)]}')
    

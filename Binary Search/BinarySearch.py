
#! Linear search:

# list1 = [12,13,14,15,16,23,45,77]
# TODO:process 1 

# def linearSearch(list1,e):
#     for x in range(len(list1)):
#         if e == list1[x]:
#             print('Hola peyechi')


# TODO:process 2- 'enupper_indexmerate' prints the index
# def linearSearch(list, n):
#     for i, e in enumerate(list):
#         if e == n:
#             return f"{n} present at {i}"
#     return -1


# print(linearSearch(list1,45))


#! Binary search:

def biSear(list, n):
    left_index = 0
    upper_index = len(list)-1
    mid_index = 0

    while left_index <= upper_index:
        mid_index = (left_index + upper_index)//2  #? '//' is for integer division
        mid_number = list[mid_index]

        if mid_number == n:
            return (mid_index)
            
        if mid_number < n:
            left_index = mid_index + 1
        else: #else case is: mid_number > n
            upper_index = mid_index - 1
                        
    return -1


list2 = [12,13,14,15,16,23,45,77]
index1 = biSear(list2, 485)
index2 = biSear(list2, 45)
print(f"Number found at {index1} using binary search")
print(f"Number found at {index2} using binary search")

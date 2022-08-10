# *****************FIND MAXIMUM*********************
def findMaxNum(list1):
    max = list1[0]
    
    for x in range(len(list1)):
        if list1[x] > max:
            max = list1[x]

    print(max)




# *****************FIND MINIMUM*********************
def findMinNum(list1):
    min = list1[0]
    
    for x in range(len(list1)):
        if list1[x] < min:
            min = list1[x]

    print(min)


newList = [11,12,13,66,14,15,-55,111]
findMaxNum(newList)
findMinNum(newList)

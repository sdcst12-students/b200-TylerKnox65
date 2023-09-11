#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = []
    for i in myList:
        
        if float(i).is_integer():
        
            integers.append(i)
     
    print(integers)
    return integers

def getFactor(myList,number):
    # myList : expected list or tuple
    # number : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
    myList = list(myList)
    for i in myList:
        try:
            if number % i == 0:
                factors.append(i)
        except:
            pass
    print(factors)
    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = []
    for i in myList:
        if i < 0:
            negatives.append(i)

    print(negatives)
    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in both lists
    # the intersection of the 2 number sets
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    common.sort()
    return common

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    union = []
    l1 = len(list1)
    l2 = len(list2)
    
    ''' 
    try:

        #if l1 >= l2:
        for i in list1:
                if i in list2:
                    pass
                else:
                    union.append(i)
                    #☻
        #else:
        for i in list2:
                if i in list1:
                    pass
                else:
                    union.append(i)
        for i in union:
            if 
    except Exception as e:
        print(e)
    '''

    for i in list1:
        union.append(i)
    for i in list2:
        if i in union:
            pass
        else:
            union.append(i)
    union.sort()
    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    
    for i in list2:
        if i in list1:
            list1.insert(list1.index(i), i)
        else:
            list1.append(i)
    return list1


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try:
        assert getIntegers([3,4,1.2,1.3,5]) == [3,4,5]
        assert getFactor(range(10),12) == [1,2,3,4,6]
        assert getNegatives([-3,-1,0,1,4]) == [-3,-1]
        print("pass")
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        print("pass")
        assert getIntersection(easy1,easy2) == [2,4,6]
        print("pass")
        assert getMerge(easy1,easy2) == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except Exception as e:
        print(f"At least 1 assertion failed, {e}")

if __name__ == "__main__":
    main()

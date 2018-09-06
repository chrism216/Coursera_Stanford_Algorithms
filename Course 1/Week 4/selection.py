import random

def RSelect(mylist, ith_element, pivot_type='left'):
    return partition(mylist, ith_element, 0, len(mylist), pivot_type)

def partition(mylist, ith_element, left, right, pivot_type, comparisons=0):
    if ith_element >= len(mylist):
        raise ValueError("ith element out of bounds")

    # Base case
    if right - left <= 1:
        return mylist[ith_element]

    else:
        choose_pivot(mylist, left, right, pivot_type='left') # place desired pivot in front
        pivot = mylist[left]

        i = left + 1
        for j in range(left + 1, right):
            if mylist[j] < pivot:
                mylist[j], mylist[i] = mylist[i], mylist[j]
                i += 1

        pivot_position = i - 1
        mylist[left], mylist[pivot_position] = mylist[pivot_position], mylist[left]
        
        # i - 1 is now the position of the pivot
        if pivot_position == ith_element:
            return mylist[pivot_position]
        elif pivot_position > ith_element:
            return partition(mylist, ith_element, left, pivot_position, pivot_type=pivot_type)
        elif pivot_position < ith_element:
            return partition(mylist, ith_element, pivot_position + 1, right, pivot_type=pivot_type)


def choose_pivot(mylist, left, right, pivot_type):
    if pivot_type == 'first':
        # nothing to do here. pivot is already in front
        pass
    elif pivot_type == 'last':
        mylist[left], mylist[right - 1] = mylist[right - 1], mylist[left]
    elif pivot_type == 'median':
        mid = left + ((right - 1) - left) // 2
        if ((mylist[left] < mylist[mid] and mylist[mid] < mylist[right - 1]) 
            or (mylist[right - 1] < mylist[mid] and mylist[mid] < mylist[left])):
            # mid position is pivot
            mylist[left], mylist[mid] = mylist[mid], mylist[left]
        elif ((mylist[left] < mylist[right - 1] and mylist[right - 1] < mylist[mid]) 
            or (mylist[mid] < mylist[right - 1] and mylist[right - 1] < mylist[left])):
            # right position is pivot
            mylist[left], mylist[right - 1] = mylist[right - 1], mylist[left]
    elif pivot_type == 'random':
        rand_pos = random.randint(left, right - 1)
        mylist[left], mylist[rand_pos] = mylist[rand_pos], mylist[left]
        

if __name__ == "__main__":
    n = 15 #array length
    ith_element = 9
    mylist = [random.randrange(0, n) for x in range(n)]
    test = sorted(mylist.copy())

    print(mylist)
    print(sorted(mylist.copy())[ith_element])
    print(RSelect(mylist, ith_element, pivot_type='random'))
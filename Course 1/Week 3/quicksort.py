import random

def quicksort(mylist, pivot_type='first'):
    comparisons = partition(mylist, 0, len(mylist), pivot_type)
    return comparisons


def partition(mylist, left, right, pivot_type, comparisons=0):
    if right - left <= 1:
        return comparisons

    else:
        choose_pivot(mylist, left, right, pivot_type) # place desired pivot in front
        pivot = mylist[left]
        i = left + 1
        for j in range(left + 1, right):
            if mylist[j] < pivot:
                mylist[j], mylist[i] = mylist[i], mylist[j]
                i += 1
        
        pivot_position = i - 1
        mylist[left], mylist[pivot_position] = mylist[pivot_position], mylist[left]
        comparisons += \
            partition(mylist, left, pivot_position, pivot_type=pivot_type) + \
            partition(mylist, i, right, pivot_type=pivot_type) + \
            right - left - 1
        return comparisons


def choose_pivot(mylist, left, right, pivot_type):
    if pivot_type == 'first':
        # nothing to do here. pivot is already in place
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
    import os

    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'QuickSort.txt')

    with open(my_file) as f:
        numbers = [int(x) for x in f]

    print(quicksort(numbers.copy(), pivot_type='first'))
    print(quicksort(numbers.copy(), pivot_type='last'))
    print(quicksort(numbers.copy(), pivot_type='median'))
    print(quicksort(numbers.copy(), pivot_type='random'))
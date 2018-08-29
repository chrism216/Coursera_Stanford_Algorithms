import random

def count_inversions_brute(mylist):
    inversions = 0
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[i]:
                inversions += 1
    return inversions

def count_inversions(mylist):
    return sort_and_count_inversions(mylist)[1]

def sort_and_count_inversions(mylist, inversions=0):
    if len(mylist) == 1:
        return mylist, 0   
    
    else:
        half = len(mylist) // 2
        sorted_left, count_left = sort_and_count_inversions(mylist[:half])
        sorted_right, count_right = sort_and_count_inversions(mylist[half:])
        sorted_list, count_split = merge_and_count_split_inversions(sorted_left, sorted_right)
        inversions += count_left + count_right + count_split
    return sorted_list, inversions


def merge_and_count_split_inversions(left, right):
    split_inversions = 0
    ordered_list = []
    i, j = 0, 0
    len_l, len_r = len(left), len(right)
    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            ordered_list.append(left[i])
            i += 1
            if i == len_l: #ran out of numbers in left list
                ordered_list += right[j:]
                break
        elif left[i] > right[j]:
            ordered_list.append(right[j])
            split_inversions += len(left[i:])
            j += 1
            if j == len_r: #ran out of numbers in right list
                ordered_list += left[i:]
                break
    return ordered_list, split_inversions
    

#Example
if __name__ == "__main__":
    n = 8 #array length
    mylist = [random.randrange(0, n) for x in range(n)]

    print(mylist)

    print(count_inversions_brute(mylist))
    print(count_inversions(mylist))
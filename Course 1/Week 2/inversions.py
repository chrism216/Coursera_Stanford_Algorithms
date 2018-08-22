import random

def count_inversions(mylist, inversions=[]):
    if len(mylist) == 1:
        return mylist, inversions
    
    else:    
        half = len(mylist) // 2
        left, left_inversions = count_inversions(mylist[:half])
        right, right_inversions = count_inversions(mylist[half:])
        inversions = left_inversions + right_inversions

        i, j = 0, 0
        ordered_list = []
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
                for k in left[i:]:
                    inversions.append((right[j], k))
                j += 1
                if j == len_r: #ran out of numbers in right list
                    ordered_list += left[i:]
                    break
    return ordered_list, inversions

#Example
n = 8 #array length
mylist = [random.randrange(0, n) for x in range(n)]

print(mylist)
print("Ordered list: %s - Inversions: %s" %(count_inversions(mylist)))
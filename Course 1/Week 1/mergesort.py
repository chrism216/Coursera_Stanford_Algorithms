import random

def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist

    else:    
        half = len(mylist) // 2
        print(half, mylist[:half], mylist[half:])
        left, right = merge_sort(mylist[:half]), merge_sort(mylist[half:])


        i, j = 0, 0
        ordered_list = []
        len_l, len_r = len(left), len(right)
        while i < len_l and j < len_r:
            if left[i] <= right[j]:
                ordered_list.append(left[i])
                i += 1
                if i == len_l: #ran out of numbers
                    ordered_list += right[j:]
                    break
            elif left[i] > right[j]:
                ordered_list.append(right[j])
                j += 1
                if j == len_r: #ran out of numbers
                    ordered_list += left[i:]
                    break
    return ordered_list


n = 10 #array length
mylist = [random.randrange(0, n) for x in range(n)]

print(mylist)
print(merge_sort(mylist))
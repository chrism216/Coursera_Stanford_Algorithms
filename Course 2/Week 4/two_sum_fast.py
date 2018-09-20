import os
import threading

def create_list(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    
    number_list = []
    with open(my_file) as f:
        for line in f:
            number_list.append((int(line.strip())))
    return number_list

def binary_search_bound(my_list, number, type=None):
    """Returns index of number in an ordered list in log n time"""
    low = 0
    high = len(my_list) - 1
    mid = low + ((high - low) // 2)
    while low <= high:
        mid = low + ((high - low) // 2)
        if number == my_list[mid]:
            return mid
        else:
            if number < my_list[mid]:
                high = mid - 1
            elif number > my_list[mid]:
                low = mid + 1
    if type == "low" and my_list[mid] < number and mid < len(my_list) - 1:
        mid += 1
    return mid

def two_sum_mod(alist, x, t_low, t_high):
    y_low = t_low - x
    y_high = t_high - x
    pos_low = binary_search_bound(alist, y_low, type="low")
    pos_high = binary_search_bound(alist, y_high)
    ys = [y for y in alist[pos_low:pos_high]]
    if alist[pos_high] <= y_high:
        ys.append(y_high)
    return ys

if __name__ == "__main__":
    numbers = create_list("algo1-programming_prob-2sum.txt")
    numbers = sorted(list(set(numbers)))
    low = -10000
    high = 10000

    total = set()
    total_list = []
    for x in numbers:
        for y in two_sum_mod(numbers, x, low, high):
            if x + y not in total:
                total_list.append((x + y, x, y))
            total.add(x + y)
    total_list = sorted(total_list)
    for t in total_list:
        print(t[0] >= low and t[0] <= high, t)

    print(len(total_list))

import os
import quicksort


this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, 'QuickSort.txt')

with open(my_file) as f:
    numbers = [int(x) for x in f]

print(quicksort.quicksort(numbers.copy(), pivot_type='first'))
print(quicksort.quicksort(numbers.copy(), pivot_type='last'))
print(quicksort.quicksort(numbers.copy(), pivot_type='median'))
print(quicksort.quicksort(numbers.copy(), pivot_type='random'))
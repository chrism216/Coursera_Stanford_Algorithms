import inversions
import os


this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, 'IntegerArray.txt')

with open(my_file) as f:
    numbers = [int(x) for x in f]


print(inversions.count_inversions(numbers))
# Don't even try brute force...
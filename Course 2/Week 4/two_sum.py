import os

def create_set(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    
    number_set = set()
    with open(my_file) as f:
        for line in f:
            number_set.add((int(line.strip())))
    return number_set

def test_2_sum(number_set, number_list, t):
    for x in number_list:
        y = t - x
        if y in number_set and y != x:
            return True
    return False

def batch_test(number_set, number_list, range_start, range_end):
    total = 0
    for t in range(range_start, range_end):
        if test_2_sum(number_set, number_list, t):
            total += 1
    return total

if __name__ == "__main__":
    # Runs for 45 minutes...
    lower_bound = -10000
    upper_bound = 10001

    number_set = create_set("algo1-programming_prob-2sum.txt")
    number_list = sorted(list(number_set))
    total = 0
    for t in range(lower_bound, upper_bound):
        if test_2_sum(number_set, number_list, t):
            total += 1
        print(t)

    print(total)


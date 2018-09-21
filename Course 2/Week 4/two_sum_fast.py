import os

def create_set(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    
    number_set = set()
    with open(my_file) as f:
        for line in f:
            number_set.add((int(line.strip())))
    return number_set

def two_sum(numbers, low, high):
    ts = set()
    top_pointer = len(numbers) - 1
    bot_pointer = len(numbers) - 1
    x_pointer = 0
    
    while x_pointer < bot_pointer:
    # for x_pointer in range(0, len(numbers)):
        while numbers[x_pointer] + numbers[bot_pointer - 1] >= low:
            bot_pointer -= 1
        
        while numbers[x_pointer] + numbers[top_pointer] > high and top_pointer > bot_pointer:
            top_pointer -= 1

        for y in numbers[bot_pointer:top_pointer]:
            ts.add(numbers[x_pointer] + y)

        if numbers[x_pointer] + numbers[top_pointer] >= low and numbers[x_pointer] + numbers[top_pointer] <= high:
            ts.add(numbers[x_pointer] + numbers[top_pointer])
        x_pointer += 1

    return ts


if __name__ == "__main__":
    numbers = sorted(list(create_set("algo1-programming_prob-2sum.txt")))

    low = -10000
    high = 10000

    my_set = two_sum(numbers, low, high)
    print(len(my_set))


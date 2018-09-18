import os
from collections import defaultdict
import heapq


def create_list(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    
    list = []
    with open(my_file) as f:
        for line in f:
            list.append(int(line.strip()))
    return list

def median_maintenance(item, low_heap, high_heap):
    """Inserts an item into corresponding heap and returns the median"""
    # If heaps are empty
    if not high_heap and not low_heap:
        heapq.heappush(high_heap, item)
        return item
    
    # Insert into correct place
    if item > high_heap[0]:
        heapq.heappush(high_heap, item)
    else:
        heapq.heappush(low_heap, -item)

    # Balance heaps:
    if len(low_heap) < len(high_heap):
        while len(low_heap) < len(high_heap) - 1:
            transfer_item = heapq.heappop(high_heap)
            heapq.heappush(low_heap, -transfer_item)
    elif len(high_heap) < len(low_heap):
        while len(high_heap) < len(low_heap): 
            transfer_item = -heapq.heappop(low_heap)
            heapq.heappush(high_heap, transfer_item)
    
    if (len(high_heap) + len(low_heap)) % 2 == 0:
        return -low_heap[0]
    else:
        return high_heap[0]

if __name__ == "__main__":
    items = create_list("Median.txt")
    low_heap = []
    high_heap = []
    median_sum = 0
    for item in items:
        median_sum += median_maintenance(item, low_heap, high_heap)
    print(median_sum % 10000)
        
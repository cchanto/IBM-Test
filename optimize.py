from time import perf_counter_ns

def countUniques(nums):
    unique_nums = set(nums)
    return len(unique_nums)

def improvedCountUniques(nums):
    unique_nums = {}
    for num in nums:
        unique_nums[num] = True
    return len(unique_nums)

def runProc(func_to_call, scale=20):
    # Hardcoded (known) test array base
    test_array = [15, 16, 16, 17, 16, 9, 0, 19, 7, 17, 19, 2, 5, 18, 12, 5, 10, 19, 13, 7, 9, 8, 2, 0, 0, 10, 1, 17, 15, 16, 19, 5, 8, 1, 5, 6, 14, 8, 18, 4, 8, 19, 17, 10, 17, 3, 15, 11, 10, 9, 11, 6, 7, 3, 9, 11, 4, 14, 18, 19, 0, 4, 18, 18, 14, 15, 6, 16, 15, 5, 0, 18, 2, 19, 12, 5, 16, 17, 13, 10, 12, 3, 8, 10, 13, 5, 2, 12, 9, 9, 16, 15, 7, 0, 5, 1, 12, 18, 16, 13, 6, 1, 11, 1, 15, 8, 12, 16, 4, 9, 10, 2, 9, 3, 1, 18, 10, 7, 16, 1, 18, 4, 1, 0, 18, 5, 1, 6, 16, 4, 0, 11, 17, 6, 16, 5, 1, 7, 0, 5, 6, 9, 19, 15, 3, 13, 3, 10, 11, 5, 1, 6, 7, 10, 17, 9, 5, 19, 9, 11, 1, 13, 10, 10, 3, 1, 4, 11, 10, 4, 15, 11, 15, 3, 12, 12, 5, 9, 7, 5, 6, 1, 11, 5, 19, 6, 18, 2, 14, 19, 4, 4, 5, 0, 3, 0, 15, 5, 2, 5, 15, 18, 17, 9, 6, 17, 12, 4, 5, 2, 6, 18, 16, 6, 10, 3, 14, 19, 12, 1, 4, 13, 11, 15, 2, 15, 5, 0, 14, 9, 3, 12, 5, 11, 11, 15, 3, 12, 14, 15, 15, 0, 16, 6, 0, 4, 4, 15, 11, 3, 2, 1, 1, 6, 3, 6, 12, 4, 16, 7, 2, 2, 14, 1, 13, 4, 17, 19, 7, 9, 1, 1, 15, 11, 9, 1, 1, 7, 15, 5, 11, 15, 13, 4, 13, 1, 18, 9, 6, 16, 13, 4, 0, 8, 7, 1, 8, 12, 18, 12]
    # Scale test array (extending test times)
    test_array *= 2**scale
    # Set start timer
    time_start = perf_counter_ns()
    # Run provided function with scaled test base
    uniques = func_to_call(test_array)
    # Set end timer
    time_end = perf_counter_ns()
    # Print result
    print(f'Unique numbers: {uniques} calculated in {time_end - time_start} nanoseconds (test base: {len(test_array)})')


runProc(countUniques)

# Create a new function that optimizes countUniques
# This optimized version uses a dictionary to track unique numbers, which can be more efficient than using a set
def improvedCountUniques(nums):
    unique_nums = {}
    for num in nums:
        unique_nums[num] = True
    return len(unique_nums)

# Append another call to runProc and show performance gain
runProc(improvedCountUniques)

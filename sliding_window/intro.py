
"""
Summary.

In many problems we are asked to find or
calculate something among a contigous 
subarray of a given size (sliding window problems)
"""


# Problem: Given an array, find the average of all contiguous subarrays of size 'K' in it
# Array: [1,3,2,6,-1,4,1,8,2], K=5


def find_averages_of_subarrays_brute_force(K, arr):
    """Sliding window brute-force."""
    result = []
    for i in range(K):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        result.append(_sum/K) # calculate average

    return result

def find_averages_of_subarrays_sliding_window(K, arr):
    """Sliding window brute-force."""
    result = []
    windowSum, windowStart = 0.0, 0
    for i in range(len(arr)):
        windowSum += arr[i] # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if i >=K - 1:
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result
            






print(find_averages_of_subarrays_brute_force(5, [1,3,2,6,-1,4,1,8,2]))
print(find_averages_of_subarrays_sliding_window(5, [1,3,2,6,-1,4,1,8,2]))
from collections import Counter

def intersect(nums1, nums2):
    res=[]
    # Count the occurrences of each element in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    print(count1)
    print(count2)
    a=[]
    # Find the intersection of the two counters
    intersection = count1 & count2
    print(intersection)
    # Convert the intersection counter to a list
    result = []
    for element in intersection.elements():
        result.append(element)
    return result
# Example 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]

# Example 2
nums1 = [4, 9,8, 5,4]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [4, 9] or [9, 4]

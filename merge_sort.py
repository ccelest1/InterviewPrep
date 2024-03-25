"""
for MS, we need to initialize a merge function and a mergeSort function that invokes both merge and mergeSort
"""


def mergeSort(arr):

    # sort arrays based on comparison between elements iterating at each to find smallest
    def merge(arr1, arr2):
        i = j = 0
        results = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                results.append(arr1[i])
                i += 1
            else:
                results.append(arr2[j])
                j += 1
        # Append remaining elements of arr1 and arr2
        # extend used to append several elements and takes iterable and adds them individually
        results.extend(arr1[i:])
        results.extend(arr2[j:])
        return results

    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    print(left)
    right = arr[middle:]
    print(right)
    return merge(mergeSort(left), mergeSort(right))


print(mergeSort([4, 3, 2, 1]))
print(mergeSort([1, 12, 5, 11, 200, 1000, 10]))

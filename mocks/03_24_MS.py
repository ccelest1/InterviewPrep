def list_dict_MS(arr, col, order):

    def merge(arr1, arr2, col, order):
        i = j = 0
        len1 = len(arr1)
        len2 = len(arr2)
        results = []
        while i < len1 and j < len2:
            if (order == "ascending" and arr1[i][col] < arr2[j][col]) or (
                order == "descending" and arr[i][col] > arr2[j][col]
            ):
                results.append(arr1[i])
                i += 1
            else:
                results.append(arr2[j])
                j += 1
        results.extend(arr1[i:])
        results.extend(arr2[j:])
        return results

    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return merge(
        list_dict_MS(left, col, order), list_dict_MS(right, col, order), col, order
    )


print(
    list_dict_MS(
        [{"a": 1, "b": 2}, {"a": 2, "b": 1}, {"a": 1, "b": 2}], "a", "ascending"
    )
)
# [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a' : 2, 'b': 1}]

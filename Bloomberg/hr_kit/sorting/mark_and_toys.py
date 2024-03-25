"""
Given list of toy prices, amt to spend
Return max number of gifts to be purchased
Toys can only be purchased once

prices = 1,2,3,4, k = 7
Max # of items to be purchased is 3

toy can't be bought several times

(1) sort the array, array will always be unsorted more often that the odds are its sorted
(2) then have a (a) purchases = [], append to purchases, (i) while sum<k, increment else break -> return len(purchases) or bill = 0, purchases = 0, bill+=item, purchases+=1 return purchases while sum<k
"""


def merge_sort(arr):
    # make sure for base case, so recursion terminates
    if not arr or len(arr) < 2:
        return arr

    def merge(arr1, arr2):
        i = j = 0
        len1 = len(arr1)
        len2 = len(arr2)
        results = []
        while i < len1 and j < len2:
            if arr1[i] < arr2[j]:
                results.append(arr1[i])
                i += 1
            else:
                results.append(arr2[j])
                j += 1
        results.extend(arr1[i:])
        results.extend(arr2[j:])
        return results

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def maximumToys(prices, k):

    if len(prices) == 1:
        if prices[0] > k:
            return 0
        else:
            return prices[0]

    sorted_prices = merge_sort(prices)
    purchases = 0
    bill = 0

    while bill < k and purchases < len(sorted_prices):
        bill += sorted_prices[purchases]
        if bill > k:
            break
        purchases += 1

    return purchases


print(maximumToys([1, 2, 3, 4], 7))
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))

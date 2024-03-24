"""
left rotation is essentially an array with elements being shifted to the left by 1
given an input of array and number of rotations to occur we need to output the resultant array

input:
    arr: list[int], n: int (# of rotations)
what this problem really boils down to is
every rotation:
    (inside v1)
     n = len(arr) - 1
     first index, goes to end ->
        arr_copy = arr
        first = arr.pop()
        arr.push(first)
and this exact op has to occur n times:
    counter = 0
    while counter < n:
        counter+=1
but the tc won't be great

maybe using two pointer we can achieve better tc
  start, end = 0, len(arr) - 1
  while start<=end: // or within b+1 operations
    [perform swap between start and end]
    start+=1
"""


def rotLeft(a: list[int], b: int) -> list[int]:
    if not a or len(a) < 2:
        return a
    counter = 0
    while counter < b:
        first = a.pop(0)
        a.append(first)
        counter += 1
    return a


# review this
def rotLeft2(a: list[int], b: int) -> list[int]:
    if not a or len(a) < 2:
        return a

    def swap(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    N = len(a) - 1
    a_copy = a
    # we know that given len(a) and b are constant that we are going to have a b%len(a) permutations give or take (finite! so limit b to be less than length of a)
    actual_rotations = b % (N + 1)  # N+1 as it is the non-0 index length

    # perform swapping ops three times, left then right then entire array using modulo remainder
    swap(a_copy, 0, actual_rotations - 1)
    swap(a_copy, actual_rotations, N)
    swap(a_copy, 0, N)

    return a_copy


print(rotLeft2([1, 2, 3], 4))
print(rotLeft2([1, 2, 3, 4, 5], 4))

"""
start = 0, end = len(a) - 1
window -> 1 -> end, copy of 1 to end
rotations -> start to end
[1,2,3,4,5]
[5,2,3,4,1]
[5,1,3,4,2]
[5,1,2,4,3]
[5,1,2,3,4] (if start == end ) -> restart start at 0

[1,2,3]
[2,3,1]
[3,1,2]
[1,2,3]
[2,3,1]
"""

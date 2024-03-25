"""
Provide a function that takes in a list of dictionaries, a column name, and a flag for 'ascending' or 'desceding' and return the same list with the entries sorted by the column name in the specified order.

You can assume that the column in question is numeric and exists. You can also assume that the list is not empty.

Please don't use any built in Python sorting functions.

Example:

Input:
   (0)                (1)              (2)
[{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 2}]
column_name = 'a'
order = 'ascending'

[0,1,2] (max/min, with the dict with the higest/lowest value dict[col])
[0,2] (tie)
if we have tie, append them w/o order concern
if there are rest we want to append them as well

Output:
[{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a' : 2, 'b': 1}]

input: list[dict], col: str, order: str ('ascending','descending')
output: list[dict] in desired asc,dsc based on specified column
function: sort dicts based in col in desired order
psedo:
res = []
wether order is asc, dsc
 if none dicts have column name, return res
 if order is asc,
   max_dict = {col:0}
   # tie with max dict
   # append max dicts
    # iterate down
   # if you have ties, handle dicts with tied highest or lowest
   if tie, then append dicts that have that max/min value
   true asc, dict[col] highest being added first
    if dict[col]>max_dict[col]:
     max_dict = dict
    res.append(max_dict)
    # update list or increment down to remaining dictionaries that have lesser values -> dictionaries that don't have column
    # append all form highest until we get to 0
 if order is dsc,
   min_dict = {col:100000}
    if dict[col]<min_dict[col]:
     min_dict = dict
     # (1) either pop to update
     # (2) iterate up from min, until we encounter no dictionaries
"""


# too contrive, overly complex
def sort_list_dictionaries(dict_list: list[dict], col: str, order: str):
    res = []
    if order == "descending":
        max_dict = {col: 0}
        for dict in dict_list:
            if dict[col] > max_dict[col]:
                max_dict = dict
                print(f"this is max col {max_dict[col]}")
                print(f"this is current col {dict[col]}")
            # address edge case for ties for max_dicts
            res.append(max_dict)
        counter_value = max_dict[col] - 1
        for dict in dict_list:
            while counter_value >= 0:
                if dict[col] == counter_value:
                    res.append(dict)
                counter_value -= 1


def bubbleSort(arr, col, order):
    def swap(arr, first, last):
        arr[first], arr[last] = arr[last], arr[first]
        return arr

    for i in range(len(arr), 0, -1):
        for j in range(0, i - 1, 1):
            # if arr[j][col]>ar[j+1][col]
            """
            if order = 'ascending':
              if arr[j][col]>arr[j+1][col]:
                ... swap
            else:
              if arr[j][col]<arr[j+1][col]:
                ... swap
            """
            """
      if (order == 'ascending' and arr[j][col]>arr[j+1][col]) or \
      (order == 'descending and arr[j][col]<arr[j+1][col]):
        swap(...)
      """
            if arr[j][col] > arr[j + 1][col]:
                swap(arr, j, j + 1)
    return arr


print(bubbleSort([{"a": 4}, {"a": 6}, {"a": 1}], "a", "ascending"))


# return res

# elif order == 'descending':
#   min_dict = {f'{col}':'Infinity'}

# print(sort_list_dictionaries(
#   [
#     {'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 2}
#   ],
#   'a',
#   'descending'
# ))

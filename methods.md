# Methods useful for Interviews
## Python
### Sort
```py
# example of MyFunc
def myFunc(e):
    return len(e)
list.sort(
    reverse = True|False # reverse = True, sort list in descending order
    key = myFunc # indicate sorting criteria
)
```
### Lambda
```py
# lambda fxn = small anon function, takes in a number of arguments and can only have 1 expression
# lambda arguments : expression

# returns sum of three numbers
x = lambda a,b,c:a+b+c
print(x(1,2,3))

#function that doubles number
def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)
print(mydoubler(11))
```
### Sorted
```py
'''
Returns sorted list fo specified iterable obj
- Can specify ascending/descending order, strings sorted alphabetically and numbers are sorted numerically
- Cannot sort list containing string, numeric values
'''
# syntax - sorted(iterable, key=key, reverse=reverse)
'''
iterable - req, sequence to sort list, dict, tuples
key - (optional) function executes and decides order
reverse - (optional) boolean, false = ascending, true = sort descending
'''
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
```

## Javascript
### Sort
- uses sort(compareFn) where compareFN is a fxn determining element order
    * a is first ele for comparison, b is second ele for compairson
    * - value = a is before b and vice versa, (a,b) => a - b sorts in ascending order
```js
const sorted_stars = stars.sort((a, b) => a.distance_from_earth - b.distance_from_earth)

```
### Reduce
### Map
### forEach

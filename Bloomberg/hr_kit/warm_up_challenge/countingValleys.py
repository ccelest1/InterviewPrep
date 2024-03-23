"""
- Count valleys encountered on vacation

*  During last hike that took `#steps` steps, for every step it is noted if it is uphill `U` or downhill `D` step. Hikes start and end at sea level with each step up or down representing a 1 unit of change in altitude i.e U = +1, D = -1
    Mountain = seq of consecutive steps above sea level, start with step up from sea level and end step down to sea level
    Valley = seq of steps below sea level, start with step down from sea level and ending with step up to sea level

    * given seq of up and down steps during hike -> print # of valleys walked through

    steps = [DDUUUUDD] -> hike enters valley 2 units deep, climbs mountain 2 units high then sea level
     -2 -> -1 -> 0 -> 1 -> 2 -> 1 -> 0

    input: steps(int), path(str)
    output: valleys(int)
"""


def countingValleys(steps: int, path: str) -> int:
    # relative level to sea
    level = 0
    # number of valleys
    valleys = 0
    l, r = 0, 0
    conversion = {"D": -1, "U": 1}
    if "D" not in path or len(path) < 2:
        return valleys
    while r < steps:
        level += conversion[path[r]]
        if path[r] == "D" and not level:
            l = r
        if path[r] != path[l] and not level:
            valleys += 1
            l = r + 1
        r += 1
    l = r
    return valleys


print(countingValleys(8, "UDDDUDUU"))
print(countingValleys(8, "DDUUUUDD"))
print(countingValleys(12, "DDUUDDUDUUUD"))
print(countingValleys(2, "UD"))
print(countingValleys(2, "DU"))

# to determine if in valley then (1) travel below sea level -> (2) to sea level.
# while seaLevel !== 0, -1 -> 0

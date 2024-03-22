"""
- Count valleys encountered on vacation

*  During last hike that took `#steps` steps, for every step it is noted if it is uphill `U` or downhill `D` step. Hikes start and end at sea level with each step up or down representing a 1 unit of change in altitude i.e U = +1, D = -1
    Mountain = seq of consecutive steps above sea level, start with step up from sea level and end step down to sea level
    Valley = seq of steps below sea level, start with step down from sea level and ending with step up to sea level

    * given seq of up and down steps during hike -> print # of valleys walked through

    steps = [DDUUUUDD] -> hike enters valley 2 units deep, climbs mountain 2 units high then sea level

    input: steps(int), path(str)
    output: valleys(int)
"""

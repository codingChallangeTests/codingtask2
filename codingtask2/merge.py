
def merge(intervals):
    """
    merges any overlapping intervals and returns the results as new List

    Args:
        intervals (List[List[int,int]]): a interval list with int or float values

    """
    out = []
    if not isinstance(intervals, list):
        raise TypeError('intervals type != list')

    # skip when there is no intervals
    if len(intervals) == 0:
        return []

    sorted_intervals = sorted(intervals, key=lambda d: d[0])
    step = sorted_intervals[0]
    for interval in sorted_intervals:
        if type(interval[0]) not in (float, int) or type(interval[1]) not in (float, int):
            raise TypeError('invalid interval data type input', interval)
        if interval[0] > interval[1]:
            raise ValueError('invalid interval data input', interval)

        if interval[0] > step[1]:
            out.append(step)
            step = interval
        elif interval[1] >= step[1]:
            step[1] = interval[1]

    # append last step to output
    out.append(step)

    return out

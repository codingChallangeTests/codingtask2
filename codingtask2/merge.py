
def merge(intervals):
    out = []
    sorted_intervals = sorted(intervals, key=lambda d: d[0])
    step = sorted_intervals[0]
    for interval in sorted_intervals:
        if interval[0] > step[1]:
            out.append(step)
            step = interval
        elif interval[1] >= step[1]:
            step[1] = interval[1]
        elif interval[0] >= step[0] and interval[1] <= step[1]:
            # nothing to do new data inside current merge step
            continue
        else:
            raise ValueError('unhandled case', step, interval)
    out.append(step)
    return out
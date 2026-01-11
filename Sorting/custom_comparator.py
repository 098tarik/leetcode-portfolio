def descending_sort(string):
    return sorted(string, key=lambda s: s.lower(), reverse=True)

def sort_intervals(interval):
    return sorted(interval, key=lambda time: time[1])


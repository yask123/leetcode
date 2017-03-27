

def min_time_difference(arr):

    augment_time(arr)
    arr.sort()
    min_difference = float('inf')

    for i in range(len(arr) - 1):
        min_difference = min(min_difference, time_difference(arr[i], arr[i + 1]))

    return min_difference




def time_difference(a, b):

    a_mins = to_minutes(a)
    b_mins = to_minutes(b)

    return abs(b_mins - a_mins)



def to_minutes(time_in_h_m):
    hours, minutes = time_in_h_m.split(':')

    hours = int(hours) * 60
    time_in_m = hours + int(minutes)
    return time_in_m


def augment_time(arr):
    for each in arr:
        h,m = map(each.split(':'), int)
        h = 24 - h
        m = 60 - m
        arr.append(str(h) + ':'+ str(m))



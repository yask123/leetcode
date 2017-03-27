arr = [0,0,0,1,2,3]


def push_zero_to_end(arr):
    w_i = 0
    r_i = 0


    while r_i < len(arr):
        if arr[w_i] == 0:
            if arr[r_i] == 0:
                r_i += 1
            else:
                arr[w_i] = arr[r_i]
                w_i += 1
                r_i += 1
        elif arr[r_i] == 0:
            r_i += 1
        else:
            arr[w_i] = arr[r_i]
            r_i += 1
            w_i += 1

    for i in range(w_i, len(arr)):
        arr[i] = 0



push_zero_to_end(arr)
print arr


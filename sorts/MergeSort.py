def merge(x, y):
    out = list()
    i, j = (0, 0)
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            out.append(x[i])
            i += 1
        else:
            out.append(y[j])
            j += 1
    while i < len(x):
        out.append(x[i])
        i += 1
    while j < len(y):
        out.append(y[j])
        j += 1
    return out


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    right = mergesort(arr[:half])
    left = mergesort(arr[half:])
    return merge(right, left)


arr = [1, 2, 3, 10, 20, 5, 5, 3, 2, 6, 6, 8, 11, 11, 11]
print(mergesort(arr))

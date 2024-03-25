def merge(x, y):
    # this step happens in O(n) time
    out = []
    i, j = (0, 0)
    count = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            out.append(x[i])
            i += 1
        else:
            out.append(y[j])
            count += (len(x) - i)
            j += 1
    while i < len(x):
        out.append(x[i])
        i += 1
    while j < len(y):
        out.append(y[j])
        j += 1
    return [out, count]


def mergesort(array):
    if len(array) <= 1:
        return [array, 0]
    half = len(array) // 2
    right = mergesort(array[:half])
    left = mergesort(array[half:])
    combine = merge(right[0], left[0])
    return [combine[0], right[1] + left[1] + combine[1]]
    # return merge(right[0], left[0])


arr = [6, 5, 4, 3, 2, 1]
print(mergesort(arr))

# string compression

def compress_string(stringArray):

    if not stringArray or len(stringArray) <= 1:
        return stringArray

    prev = stringArray[0]
    outList = list()
    count = 1
    for cur in stringArray[1:]:
        if cur == prev:
            count += 1
        else:
            outList.append(prev)
            outList.append(str(count))
            prev = cur
            count = 1
    outList.append(prev)
    outList.append(str(count))

    if len(outList) > len(stringArray):
        return stringArray
    return ''.join(outList)

stringArray = 'aabcccccaaa'
print(compress_string(stringArray))
stringArray = 'abc'
print(compress_string(stringArray))
stringArray = 'aabc'
print(compress_string(stringArray))
stringArray = 'aaabbc'
print(compress_string(stringArray))

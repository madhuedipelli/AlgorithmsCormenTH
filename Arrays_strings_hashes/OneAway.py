def one_away(word1, word2):
    dict1 = dict()
    dict2 = dict()

    for i in word1:
        if i in dict1:  # word1 length
            dict1[i] += 1
        else:
            dict1[i] = 1
    for j in word2:  # word2 length
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1
        if j in dict1:
            dict1[j] -= 1
            dict2[j] -= 1

    word1_sum = sum(dict1.values())  #
    word2_sum = sum(dict2.values())  # n

    if (word1_sum == 0 and word2_sum == 1) or (word1_sum == 1 and (word2_sum == 0 or word2_sum == 1)):
        return True
    return False


print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))

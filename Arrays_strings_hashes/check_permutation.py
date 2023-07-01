# given two strings, check if one is permutation of other

# key permutation is different order of same items
from collections import defaultdict,Counter
import unittest

# to check counter function in collections

def check_permutation_ctci(str1,str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

def check_permutation(string1,string2):
    #length should be same
    if len(string1) != len(string2):
        return False
    count_str1 = defaultdict()

    for i in range(len(string2)):
        if string1[i] in count_str1:
            count_str1[string1[i]] += 1
        else:
            count_str1[string1[i]] = 1
        if string2[i] in count_str1:
            count_str1[string2[i]] -= 1
        else:
            count_str1[string2[i]] = -1
    #print(count_str1)
    for i in count_str1.values():
        if i < 0:
            return False
    return True

print(check_permutation('yellow','lowlem'))


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

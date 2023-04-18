# algo to check if string has all unique characters
from collections import defaultdict
import unittest


def check_unique(string):
    check_dict = defaultdict()

    if string:
        for i in string:
            if i in check_dict:
                return False
            check_dict[i] = 1
        return True
    return True

def check_unique_nodict(string):
    if len(string)> 128:
        return False
    u_check = [ False for i in range(128)]

    for i in (string):
        char_ord = ord(i)
        if u_check[char_ord]:
            return False
        u_check[char_ord] = True
    return True
test = 'teaser'

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = check_unique_nodict(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_unique_nodict(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

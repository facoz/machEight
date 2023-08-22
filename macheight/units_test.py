import unittest
import find_pairs as a

class TestFindPairsFunction(unittest.TestCase):

    def test_positive_case(self):
        input_list = [2, 4, 3, 1, 5]
        target_sum = 6
        expected_result = [(2, 4), (1, 5)]
        self.assertEqual(a.find_pairs(input_list, target_sum), expected_result)

    def test_no_match_case(self):
        input_list = [1, 2, 3, 4, 5]
        target_sum = 10
        expected_result = []
        self.assertEqual(a.find_pairs(input_list, target_sum), expected_result)

    def test_duplicates(self):
        input_list = [2, 2, 4, 3, 1, 5, 1]
        target_sum = 6
        expected_result = [(2, 4), (1, 5), (5, 1)]
        self.assertEqual(a.find_pairs(input_list, target_sum), expected_result)

if __name__ == '__main__':
    unittest.main()

import unittest

from app.validate_data import check_number_of_fields


class TestValidateData(unittest.TestCase):

    def test_check_number_of_fields(self):
        valid_lst = [[1, 2, 3], [4, 5, 6]]
        result = check_number_of_fields(valid_lst, 3)
        self.assertFalse(len(result[0]))
        invalid_lst = [[1, 2, 3], [4, 5]]
        result = check_number_of_fields(invalid_lst, 3)
        self.assertTrue(len(result[0]))


if __name__ == '__main__':
    unittest.main()

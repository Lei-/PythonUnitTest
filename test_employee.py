import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.michael = Employee('Michael', 'Zhang', 100000)
        self.jim = Employee('Jim', 'Wong', 0)

    def test_email(self):
        self.assertEqual(self.michael.email, 'Michael.Zhang@email.com')

        self.michael.first_name = 'Lei'
        self.assertEqual(self.michael.email, 'Lei.Zhang@email.com')

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            # Test happy path #
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            result = self.michael.monthly_schedule('May')

            mocked_get.assert_called_with('http://company.com/Zhang/May')
            self.assertEqual(result, 'Success')

            # Test happy path #
            mocked_get.return_value.ok = False

            result = self.jim.monthly_schedule('June')

            mocked_get.assert_called_with('http://company.com/Wong/June')
            self.assertEqual(result, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

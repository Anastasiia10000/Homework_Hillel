from lesson_13.homeworks import computer_price
import unittest


class TestComputerPrice(unittest.TestCase):
    def setUp(self):
        self.credit_period = 18
        self.credit_per_month = 1179
        print(f"\n🔄 Running test: {self._testMethodName}")

    def tearDown(self):
        self.credit_period = None
        self.credit_per_month = None
        print(f"\n✅ Test completed: {self._testMethodName}")

    def test_assertEqual(self):
        expected_result = 18 * 1179
        actual_result = computer_price(self.credit_period, self.credit_per_month)
        self.assertEqual(expected_result, actual_result)

    def test_return_type_is_int(self):
        actual_result = computer_price(self.credit_period, self.credit_per_month)
        self.assertIsInstance(actual_result, int)

    def test_zero_period(self):
        self.assertEqual(0, computer_price(0, self.credit_per_month))

    def test_zero_payment(self):
        self.assertEqual(0, computer_price(self.credit_period, 0), msg="Value should be zero")

    def test_negative_values(self):
        actual_result1 = computer_price(-1, self.credit_per_month)
        actual_result2 = computer_price(self.credit_period, -100)
        self.assertLess(actual_result1, 0)
        self.assertLess(actual_result2, 0)

if __name__ == '__main__':
    unittest.main()
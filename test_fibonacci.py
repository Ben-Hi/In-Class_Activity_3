import unittest
import fibonacci

class Test_Fibonacci(unittest.TestCase):
    def test_base_zero(self):
        self.assertEqual(fibonacci.fib_series(0), 0)

    def test_base_one(self):
        self.assertEqual(fibonacci.fib_series(1), 1)

    def test_two(self):
        self.assertEqual(fibonacci.fib_series(2), 1)

    def test_eight(self):
        self.assertEqual(fibonacci.fib_series(8), 21)

if __name__ == '__main__':
    unittest.main()
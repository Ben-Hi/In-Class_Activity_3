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

#if __name__ == '__main__':
#    unittest.main()


def test_fib_series_base_zero():
    assert fibonacci.fib_series(0) == 0

def test_fib_series_eight():
    assert fibonacci.fib_series(8) == 21

def test_factorial_base_zero():
    assert fibonacci.factorial(0) == 1

def test_factorial_base_one():
    assert fibonacci.factorial(1) == 1

def test_factorial_five():
    assert fibonacci.factorial(5) == 120
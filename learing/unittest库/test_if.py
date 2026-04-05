import unittest
import if_example

class Test_if(unittest.TestCase):
    def test_if_1(self):
        result = if_example.check_if(1)
        self.assertEqual(result, "a==1")

    def test_if_2(self):
        result = if_example.check_if(5)
        self.assertEqual(result, "a!=1")

if __name__ == '__main__':
    unittest.main()
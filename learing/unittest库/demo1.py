import unittest


def add_number(x,y):
    return x+y

def subtract_number(x,y):
    return x-y
def multiply_number(x,y):
    return x*y
def divide_number(x,y):
    return x/y

class Test_addition(unittest.TestCase):
    def test_add_numbers_int(self):
        sum=add_number(1,2)
        self.assertEqual(sum,3)

    def test_subtract_numbers_int(self):
        sum=subtract_number(1,2)
        self.assertEqual(sum,-1)

    def test_multiply_numbers_int(self):
        sum=multiply_number(1,2)
        self.assertEqual(sum,2)

    def test_divide_numbers_int(self):
        sum=divide_number(1,2)
        self.assertEqual(sum,0.5)

if __name__ == '__main__':
        unittest.main()
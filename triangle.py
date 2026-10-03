'''Code to identify triangles and test cases'''
import unittest

def classify_triangle(a, b, c):
    '''
    Takes inputs as sides of a triangle and returns the
    type of triangle that the numbers would create.
    '''
    if (a==b) and (b==c):
        type = "equilateral"
    elif ((a==b) or (b==c) or (a==c)) and ((a!=b) or (b!=c) or (a!=c)):
        type = "isoceles"
    elif (a!=b) and (b!=c) and (a!=c):
        type = "scalene"

    if (a**2 + b**2) == c**2:
        type += ", right triangle"
    else:
        type += ", not a right triangle"
    return type

class TestTriangles(unittest.TestCase):
    '''Test class for testing triangles'''
    def test_triangles(self):
        '''triangle test case 1'''
        self.assertEqual(classify_triangle(3, 3, 7),("isoceles, not a right triangle"))
    def test_t(self):
        '''triangle test case 2'''
        self.assertEqual(classify_triangle(3, 4, 5),("scalene, right triangle"))
    def test_p(self):
        '''triangle test case 3'''
        self.assertEqual(classify_triangle(3, 3, 3),("equilateral, not a right triangle"))

if __name__ == '__main__':
    unittest.main()

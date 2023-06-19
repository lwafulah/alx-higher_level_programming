import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_create_square(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
    
    def test_set_attributes(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)
        s.x = 2
        s.y = 3
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
    
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)
    
    def test_display(self):
        s = Square(3, 2, 1)
        expected_output = "###\n###\n###"
        self.assertEqual(s.display(), expected_output)
    
    def test_str_representation(self):
        s = Square(4, 1, 2, 5)
        expected_str = "[Square] (5) 1/2 - 4"
        self.assertEqual(str(s), expected_str)
    
    def test_update_args(self):
        s = Square(5)
        s.update(10, 6, 2, 3)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
    
    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=8, y=4, x=2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)
    
    def test_to_dictionary(self):
        s = Square(5, 2, 3, 7)
        expected_dict = {
            'id': 7,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()


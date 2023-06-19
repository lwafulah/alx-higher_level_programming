import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_instance(self):
        """Test if a Rectangle instance can be created"""
        rectangle = Rectangle(2, 4)
        self.assertIsInstance(rectangle, Rectangle)

    def test_area(self):
        """Test the area method of Rectangle"""
        rectangle = Rectangle(3, 5)
        self.assertEqual(rectangle.area(), 15)

    def test_display(self):
        """Test the display method of Rectangle"""
        rectangle = Rectangle(3, 4)
        expected_output = "###\n###\n###\n###\n"
        with self.assertLogs() as logs:
            rectangle.display()
            self.assertEqual(logs.output[0], expected_output)

    def test_update(self):
        """Test the update method of Rectangle"""
        rectangle = Rectangle(2, 3, 4, 5, 1)
        rectangle.update(10, 5, 6, 7, 8)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle"""
        rectangle = Rectangle(3, 4, 5, 6, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertDictEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

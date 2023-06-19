import unittest
import json
from abc import ABC, abstractmethod

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_create_instance(self):
        """Test if a Base instance can be created"""
        base = Base()
        self.assertIsInstance(base, Base)

    def test_unique_ids(self):
        """Test if each Base instance has a unique ID"""
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

    def test_custom_id(self):
        """Test if a Base instance can be created with a custom ID"""
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        base1 = Base()
        base2 = Base()
        base_list = [base1, base2]
        json_string = Base.to_json_string(base_list)
        self.assertIsInstance(json_string, str)
        self.assertGreater(len(json_string), 0)

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        base_list = Base.from_json_string(json_string)
        self.assertIsInstance(base_list, list)
        self.assertEqual(len(base_list), 2)
        self.assertIsInstance(base_list[0], Base)
        self.assertIsInstance(base_list[1], Base)
    def test_save_to_file(self):
        """Test the save_to_file method"""
        base1 = Base()
        base2 = Base()
        base_list = [base1, base2]

        Base.save_to_file(base_list)

        with open("Base.json", "r") as file:
            json_string = file.read()
            decoded_list = json.loads(json_string)
            self.assertIsInstance(decoded_list, list)
            self.assertEqual(len(decoded_list), 2)

            for item in decoded_list:
                self.assertIn('id', item)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        base_list = Base.load_from_file(Base)

        self.assertIsInstance(base_list, list)
        self.assertGreaterEqual(len(base_list), 0)

        for item in base_list:
            self.assertIsInstance(item, Base)

    def test_load_from_file_nonexistent(self):
        """Test loading from a nonexistent file"""
        base_list = Base.load_from_file(Base)
        self.assertEqual(len(base_list), 0)

if __name__ == '__main__':
    unittest.main()

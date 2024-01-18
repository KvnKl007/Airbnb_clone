#!/usr.bin.python3
"""

"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        current_update_at = my_model.save()
        self.assertNotEqual(old_updated_at, current_update_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()
        my_model_str = my_model.__str__()
        self.assertIsInstance(my_model_str, str)
        self.assertIn("BaseModel", my_model_str)
        self.assertIn(my_model.id, my_model_str)
        self.assertIn(my_model.__dict__, my_model_str)


if __name__ == "__main__":
    unittest.main()
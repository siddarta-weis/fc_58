import unittest
from dataclasses import is_dataclass
from datetime import datetime
from category.domain.entities import Category

class TestCategory(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        category = Category(name='Movie', description="some description", is_active=True, created_at=datetime.now())
        self.assertTrue(is_dataclass(category))

    def test_constructor_all_parameters(self):
        created_at = datetime.now()
        category = Category(name='Movie', description="some description", is_active=True, created_at=created_at)
        self.assertEqual(category.name, "Movie")
        self.assertEqual(category.description, "some description")
        self.assertEqual(category.is_active, True)
        self.assertEqual(category.created_at, created_at)

    def test_constructor_name_parameters(self):
        category = Category(name='Movie')
        self.assertEqual(category.name, "Movie")
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

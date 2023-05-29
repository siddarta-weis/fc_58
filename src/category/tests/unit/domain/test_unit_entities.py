import unittest
from dataclasses import is_dataclass, FrozenInstanceError
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

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(name='test')
            value_object.name = 'fake id'

    def test_if_update_values(self):
        category = Category(name="book", description="a math book")
        category = category.update(name="magazine", description="a math magazine")

        self.assertEqual(category.name, "magazine")
        self.assertEqual(category.description, "a math magazine")

    def test_if_is_activated(self):
        category = Category(name="book", description="a math book", is_active=False)
        category = category.activate()

        self.assertEqual(category.is_active, True)

    def test_if_is_deactivated(self):
        category = Category(name="book", description="a math book", is_active=True)
        category = category.deactivate()

        self.assertEqual(category.is_active, False)

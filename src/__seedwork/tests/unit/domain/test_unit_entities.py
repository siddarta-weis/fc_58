import unittest
from abc import ABC
from dataclasses import is_dataclass, dataclass
from __seedwork.domain.entities import Entity
from __seedwork.domain.entities import UniqueEntityId


@dataclass(kw_only=True, frozen=True)
class StubEntity(Entity):
    prop1: str
    prop2: str


class TestEntityUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abc(self):
        self.assertIsInstance(Entity(), ABC)

    def test_properties(self):
        value1 = 'value1'
        value2 = 'value2'
        en1 = StubEntity(prop1=value1, prop2=value2)
        self.assertEqual(en1.prop1, value1)
        self.assertEqual(en1.prop2, value2)
        self.assertIsInstance(en1.unique_entity_id, UniqueEntityId)
        self.assertEqual(en1.unique_entity_id.id, en1.id)

    def test_accept_a_valid_uuid(self):
        value1 = 'value1'
        value2 = 'value2'
        uuid = 'f565e7c9-479e-4f09-97a5-f7e1276ad79a'
        entity = StubEntity(unique_entity_id=uuid, prop1=value1, prop2=value2)
        self.assertEqual(entity.id, uuid)
        self.assertDictEqual(entity.to_dict(), {"id": uuid, "prop1": value1, "prop2": value2})

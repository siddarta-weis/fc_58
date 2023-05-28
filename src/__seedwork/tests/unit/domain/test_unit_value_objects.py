import unittest
from abc import ABC
import uuid
from dataclasses import is_dataclass, FrozenInstanceError, dataclass
from unittest.mock import patch
from __seedwork.domain.value_objects import UniqueEntityId, ValueObject
from __seedwork.domain.exceptions import InvalidUuidException


@dataclass(frozen=True)
class StubOneProperty(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProperty(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_instance_of_abc(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        value = 'value'
        vo1 = StubOneProperty(value)
        self.assertEqual(vo1.prop, value)

    def test_init_prop_two_value(self):
        value1 = 'value1'
        value2 = 'value2'
        vo1 = StubTwoProperty(prop1=value1, prop2=value2)
        self.assertEqual(vo1.prop1, value1)
        self.assertEqual(vo1.prop2, value2)

    def test_convert_to_str(self):
        value1 = 'value1'
        value2 = 'value2'
        vo1 = StubOneProperty(prop=value1)
        self.assertEqual(vo1.prop, str(vo1))

        vo2 = StubTwoProperty(prop1=value1, prop2=value2)
        self.assertEqual('{"prop1": "value1", "prop2": "value2"}', str(vo2))

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value1 = 'value1'

            vo1 = StubOneProperty(prop=value1)
            vo1.id = 'fake id'


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(UniqueEntityId, '_UniqueEntityId__validate', autospec=True,
                          side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(UniqueEntityId, '_UniqueEntityId__validate', autospec=True,
                          side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
            value_object = UniqueEntityId('fa458068-fb8e-43c2-87c8-e9533e9737b7')
            mock_validate.assert_called_once()
            self.assertEqual(value_object.id, 'fa458068-fb8e-43c2-87c8-e9533e9737b7')

    def test_generated_id_when_no_passed_id_in_constructor(self):
        with patch.object(UniqueEntityId, '_UniqueEntityId__validate', autospec=True,
                          side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
            value_object = UniqueEntityId()
            mock_validate.assert_called_once()
            self.assertIsInstance(uuid.UUID(value_object.id), uuid.UUID)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = 'fake id'

    def test_convert_to_str(self):
        value_object = UniqueEntityId()
        self.assertEqual(value_object.id, str(value_object))

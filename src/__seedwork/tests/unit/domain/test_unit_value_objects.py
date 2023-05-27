import unittest
from dataclasses import is_dataclass
from unittest.mock import patch
from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.exceptions import InvalidUuidException


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(UniqueEntityId, '_UniqueEntityId__validate', autospec=True, side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()



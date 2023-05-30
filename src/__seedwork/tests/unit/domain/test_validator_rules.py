from unittest import TestCase
from __seedwork.domain.validators import ValidatorRules
from __seedwork.domain.exceptions import ValidationException


class TestValidatorRule(TestCase):
    def test_value_methods(self):
        validator = ValidatorRules("some value", "prop")
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, "some value")
        self.assertEqual(validator.prop, "prop")

    def test_required_rule(self):
        invalid_data = [
            {"value": None, "prop": "prop"},
            {"value": "", "prop": "prop"},
        ]
        for i in invalid_data:
            with self.assertRaises(
                ValidationException, msg=f"value: {i['value']}, prop: {i['prop']}"
            ) as assert_error:
                self.assertIsInstance(
                    ValidatorRules.values(i["value"], str(i["prop"])).required(),
                    ValidatorRules,
                )
            self.assertEqual(
                "The prop is required",
                assert_error.exception.args[0],
            )

        valid_data = [
            {"value": "teste", "prop": "prop"},
            {"value": "5", "prop": "prop"},
            {"value": 0, "prop": "prop"},
            {"value": 4, "prop": "prop"},
            {"value": False, "prop": "prop"},
        ]
        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], str(i["prop"])).required(),
                ValidatorRules,
                msg=f"value: {i['value']}, prop: {i['prop']}",
            )

    def test_string_rule(self):
        invalid_data = [
            {"value": 5, "prop": "prop"},
            {"value": True, "prop": "prop"},
            {"value": {}, "prop": "prop"},
            {"value": [], "prop": "prop"},
        ]
        for i in invalid_data:
            with self.assertRaises(
                ValidationException, msg=f"value: {i['value']}, prop: {i['prop']}"
            ) as assert_error:
                self.assertIsInstance(
                    ValidatorRules.values(i["value"], str(i["prop"])).string(),
                    ValidatorRules,
                )
            self.assertEqual(
                "The prop must be a string",
                assert_error.exception.args[0],
            )

        valid_data = [
            {"value": "teste", "prop": "prop"},
            {"value": "5", "prop": "prop"},
            {"value": "", "prop": "prop"},
            {"value": None, "prop": "prop"},
        ]
        for i in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(i["value"], str(i["prop"])).string(),
                ValidatorRules,
                msg=f"value: {i['value']}, prop: {i['prop']}",
            )

    def test_max_length_rule(self):
        value = "teste"
        prop = "prop"
        with self.assertRaises(
            ValidationException, msg=f"value: {value}, prop: {prop}"
        ) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values(value, prop).max_length(4),
                ValidatorRules,
            )
        self.assertEqual(
            "The property prop must be less or equal to 4",
            assert_error.exception.args[0],
        )

        self.assertIsInstance(
            ValidatorRules.values(value, prop).max_length(5),
            ValidatorRules,
            msg=f"value: {value}, prop: {prop}",
        )

    def test_boolean_rule(self):
        valid_value = True
        invalid_value = "some_value"
        prop = "prop"
        with self.assertRaises(
            ValidationException, msg=f"value: {invalid_value}, prop: {prop}"
        ) as assert_error:
            self.assertIsInstance(
                ValidatorRules.values(invalid_value, prop).boolean(),
                ValidatorRules,
            )
        self.assertEqual(
            "The property prop must be a boolean",
            assert_error.exception.args[0],
        )

        self.assertIsInstance(
            ValidatorRules.values(valid_value, prop).boolean(),
            ValidatorRules,
            msg=f"value: {valid_value}, prop: {prop}",
        )
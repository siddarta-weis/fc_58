from dataclasses import dataclass
from typing import Any
from .exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value: Any, prop: str) -> "ValidatorRules":
        return ValidatorRules(value, prop)

    def required(self) -> "ValidatorRules":
        if self.value is None or self.value == "":
            raise ValidationException(f"The {self.prop} is required")
        return self

    def string(self) -> "ValidatorRules":
        if self.value is not None and not isinstance(self.value, str):
            raise ValidationException(f"The {self.prop} must be a string")
        return self

    def max_length(self, max_length: int) -> "ValidatorRules":
        if self.value is not None and len(self.value) > max_length:
            raise ValidationException(
                f"The property {self.prop} must be less or equal to {max_length}"
            )
        return self

    def boolean(self) -> "ValidatorRules":
        if (
            self.value is not None
            and self.value is not True
            and self.value is not False
        ):
            raise ValidationException(f"The property {self.prop} must be a boolean")
        return self

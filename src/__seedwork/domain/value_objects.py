from abc import ABC
import json
from dataclasses import dataclass, field, fields
from __seedwork.domain.exceptions import InvalidUuidException
import uuid


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_name = [f.name for f in fields(self)]
        if len(fields_name) == 1:
            return str(getattr(self, fields_name[0]))
        return json.dumps({field_name: getattr(self, field_name) for field_name in fields_name})


@dataclass(frozen=True, slots=True)
class UniqueEntityId(ValueObject):
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex

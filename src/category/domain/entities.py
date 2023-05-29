from datetime import datetime
from dataclasses import dataclass, field, replace
from typing import Optional
from __seedwork.domain.entities import UniqueEntityId


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(UniqueEntityId):
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())

    def update(self, name: str, description: str):
        return replace(self, name=name, description=description)

    def activate(self):
        return replace(self, is_active=True)

    def deactivate(self):
        return replace(self, is_active=False)

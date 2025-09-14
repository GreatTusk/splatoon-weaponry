from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from . import WeaponCategoryEntity


class WeaponEntity(SQLModel, table=True):
    __tablename__ = "weapon"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    category_id: int = Field(foreign_key="weapon_category.id")

    category: "WeaponCategoryEntity" = Relationship(back_populates="weapons")

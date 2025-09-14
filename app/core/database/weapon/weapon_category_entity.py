from sqlmodel import SQLModel, Field, Relationship

from . import WeaponEntity


class WeaponCategoryEntity(SQLModel, table=True):
    __tablename__ = "weapon_category"

    id: int | None = Field(primary_key=True)
    name: str

    weapons: list["WeaponEntity"] = Relationship(back_populates="category")

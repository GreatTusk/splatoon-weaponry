from sqlmodel import SQLModel, Field


class WeaponCategoryEntity(SQLModel, table=True):
    __tablename__ = "weapon_category"

    id: int | None = Field(primary_key=True)
    name: str

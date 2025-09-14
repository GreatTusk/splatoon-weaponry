from sqlmodel import SQLModel, Field


class WeaponEntity(SQLModel, table=True):
    __tablename__ = "weapon"

    id: int | None = Field(primary_key=True)
    name: str = Field(unique=True)
    category_id: int = Field(foreign_key="weapon_category.id")
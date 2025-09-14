from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database.weapon import WeaponEntity, WeaponCategoryEntity
from .weapon_repository import WeaponRepository


class WeaponRepositoryImpl(WeaponRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity:
        result = await self.db.exec(select(WeaponEntity).where(WeaponEntity.id == weapon_id))
        return result.first()

    async def get_weapons_by_category(self, category_id: int) -> list[WeaponEntity]:
        result = await self.db.exec(select(WeaponCategoryEntity).where(WeaponCategoryEntity.id == category_id))
        category = result.first()

        if category is None:
            return []

        return category.weapons

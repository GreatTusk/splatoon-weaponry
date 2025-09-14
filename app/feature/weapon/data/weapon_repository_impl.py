from sqlalchemy.orm import joinedload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database.weapon import WeaponEntity
from .weapon_repository import WeaponRepository


class WeaponRepositoryImpl(WeaponRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity | None:
        result = await self.db.exec(
            select(WeaponEntity)
            .options(joinedload(WeaponEntity.category))
            .where(WeaponEntity.id == weapon_id)
        )
        return result.first()

    async def get_weapons_by_category(self, category_id: int) -> list[WeaponEntity]:
        result = await self.db.exec(
            select(WeaponEntity)
            .options(joinedload(WeaponEntity.category))
            .where(WeaponEntity.category_id == category_id)
        )
        return list(result.all())

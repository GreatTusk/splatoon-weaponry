from sqlalchemy.orm import joinedload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database.weapon import WeaponEntity
from .weapon_repository import WeaponRepository
from app.feature.weapon.domain.model.weapon_filter import WeaponFilter


class WeaponRepositoryImpl(WeaponRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity | None:
        result = await self.db.exec(
            select(WeaponEntity)
            .where(WeaponEntity.id == weapon_id)
            .options(joinedload(WeaponEntity.category))
        )
        return result.first()

    async def get_weapons(self, filters: WeaponFilter) -> list[WeaponEntity]:
        statement = select(WeaponEntity)

        if filters.category_id:
            statement = statement.where(WeaponEntity.category_id == filters.category_id)

        statement = statement.limit(filters.limit).offset(filters.offset).options(joinedload(WeaponEntity.category))

        result = await self.db.exec(statement)
        return list(result.all())

from app.core.database.weapon import WeaponEntity
from .weapon_service import WeaponService
from ..data import WeaponRepository


class WeaponServiceImpl(WeaponService):

    def __init__(self, weapon_repository: WeaponRepository):
        self.weapon_repository = weapon_repository

    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity | None:
        return await self.weapon_repository.get_weapon_by_id(weapon_id=weapon_id)

    async def get_weapons_by_category(self, category_id: int) -> list[WeaponEntity]:
        return await self.weapon_repository.get_weapons_by_category(category_id=category_id)

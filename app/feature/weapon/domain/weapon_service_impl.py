from .model.get_weapon_response import GetWeaponResponse
from .weapon_service import WeaponService
from app.feature.weapon.domain.model.weapon_filter import WeaponFilter
from ..data import WeaponRepository


class WeaponServiceImpl(WeaponService):

    def __init__(self, weapon_repository: WeaponRepository):
        self.weapon_repository = weapon_repository

    async def get_weapon_by_id(self, weapon_id: int) -> GetWeaponResponse | None:
        weapon = await self.weapon_repository.get_weapon_by_id(weapon_id=weapon_id)
        if weapon is None:
            return None
        return GetWeaponResponse(id=weapon.id, name=weapon.name, category=weapon.category.name)

    async def get_weapons(self, filters: WeaponFilter) -> list[GetWeaponResponse]:
        weapons = await self.weapon_repository.get_weapons(filters=filters)
        return [
            GetWeaponResponse(id=weapon.id, name=weapon.name, category=weapon.category.name)
            for weapon in weapons
        ]

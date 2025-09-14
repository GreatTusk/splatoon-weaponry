from .model.get_weapon_response import GetWeaponResponse
from .weapon_service import WeaponService
from ..data import WeaponRepository


class WeaponServiceImpl(WeaponService):

    def __init__(self, weapon_repository: WeaponRepository):
        self.weapon_repository = weapon_repository

    async def get_weapon_by_id(self, weapon_id: int) -> GetWeaponResponse | None:
        weapon = await self.weapon_repository.get_weapon_by_id(weapon_id=weapon_id)
        if weapon is None:
            return None
        return GetWeaponResponse(id=weapon.id, name=weapon.name, category=weapon.category.name)

    async def get_weapons_by_category(self, category_id: int) -> list[GetWeaponResponse]:
        weapons = await self.weapon_repository.get_weapons_by_category(category_id=category_id)
        return [
            GetWeaponResponse(id=weapon.id, name=weapon.name, category=weapon.category.name)
            for weapon in weapons
        ]

from abc import ABC, abstractmethod

from .model.get_weapon_response import GetWeaponResponse


class WeaponService(ABC):
    @abstractmethod
    async def get_weapon_by_id(self, weapon_id: int) -> GetWeaponResponse | None:
        pass

    @abstractmethod
    async def get_weapons_by_category(self, category_id: int) -> list[GetWeaponResponse]:
        pass

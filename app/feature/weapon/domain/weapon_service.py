from abc import ABC, abstractmethod

from .model.get_weapon_response import GetWeaponResponse
from app.feature.weapon.domain.model.weapon_filter import WeaponFilter


class WeaponService(ABC):
    @abstractmethod
    async def get_weapon_by_id(self, weapon_id: int) -> GetWeaponResponse | None:
        pass

    @abstractmethod
    async def get_weapons(self, filters: WeaponFilter) -> list[GetWeaponResponse]:
        pass

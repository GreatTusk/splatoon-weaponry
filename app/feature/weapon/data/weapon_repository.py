from abc import ABC, abstractmethod

from app.core.database.weapon import WeaponEntity
from app.feature.weapon.domain.model.weapon_filter import WeaponFilter


class WeaponRepository(ABC):
    @abstractmethod
    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity | None:
        pass

    @abstractmethod
    async def get_weapons(self,  filters: WeaponFilter) -> list[WeaponEntity]:
        pass

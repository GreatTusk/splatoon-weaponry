from abc import ABC, abstractmethod

from app.core.database.weapon import WeaponEntity


class WeaponRepository(ABC):
    @abstractmethod
    async def get_weapon_by_id(self, weapon_id: int) -> WeaponEntity | None:
        pass

    @abstractmethod
    async def get_weapons_by_category(self, category_id: int) -> list[WeaponEntity]:
        pass

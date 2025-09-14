from .weapon_service import WeaponService
from ..dependencies import WeaponRepositoryDep


class WeaponServiceImpl(WeaponService):

    def __init__(self, weapon_repository: WeaponRepositoryDep):
        self.weapon_repository = weapon_repository
from fastapi import APIRouter

from app.feature.weapon.dependencies import WeaponServiceDep

router = APIRouter(prefix="/weapon")


@router.get("/{weapon_id}")
async def get_weapon_by_id(weapon_id: int, weapon_service: WeaponServiceDep):
    return await weapon_service.get_weapon_by_id(weapon_id=weapon_id)

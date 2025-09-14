from typing import Annotated

from fastapi import APIRouter, Query

from app.feature.weapon.domain.model.weapon_filter import WeaponFilter
from app.feature.weapon.dependencies import WeaponServiceDep
from app.feature.weapon.domain.model.get_weapon_response import GetWeaponResponse

router = APIRouter(prefix="/weapon")


@router.get("/{weapon_id}", response_model=GetWeaponResponse)
async def get_weapon_by_id(weapon_id: int, weapon_service: WeaponServiceDep):
    return await weapon_service.get_weapon_by_id(weapon_id=weapon_id)


@router.get("/", response_model=list[GetWeaponResponse])
async def get_weapons(filters: Annotated[WeaponFilter, Query()], weapon_service: WeaponServiceDep):
    return await weapon_service.get_weapons(filters=filters)

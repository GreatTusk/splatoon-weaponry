from typing import Annotated

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database.config import get_session
from .data import WeaponRepositoryImpl, WeaponRepository
from .domain import WeaponServiceImpl, WeaponService


def get_weapon_repository(db: Annotated[AsyncSession, Depends(get_session)]) -> WeaponRepository:
    return WeaponRepositoryImpl(db)


WeaponRepositoryDep = Annotated[WeaponRepository, Depends(get_weapon_repository)]


def get_weapon_service(repository: WeaponRepositoryDep) -> WeaponService:
    return WeaponServiceImpl(repository)


WeaponServiceDep = Annotated[WeaponService, Depends(get_weapon_service)]

from pydantic import BaseModel


class GetWeaponResponse(BaseModel):
    id: int
    name: str
    category: str
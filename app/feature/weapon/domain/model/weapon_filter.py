from pydantic import BaseModel, Field

from app.shared.controller.pagination_filter import PaginationFilter


class WeaponFilter(BaseModel, PaginationFilter):
    category_id: int | None = Field(default=None)
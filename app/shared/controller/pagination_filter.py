from pydantic import Field


class PaginationFilter:
    limit: int = Field(20, gt=0, le=100)
    offset: int = Field(0, ge=0)

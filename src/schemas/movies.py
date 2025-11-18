
from pydantic import BaseModel

from typing import List, Optional


class MovieSchema(BaseModel):
    id: int
    name: str
    date: str
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: int
    revenue: int
    country: str

    class Config:
        orm_mode = (
            True  
        )


class MovieListResponseSchema(BaseModel):
    movies: List[MovieSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int


class MovieDetailResponseSchema(MovieSchema):
    pass

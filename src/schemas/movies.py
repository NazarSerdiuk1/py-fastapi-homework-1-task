
from pydantic import BaseModel

from typing import List, Optional


# Схема для одного фільму
class MovieDetailResponseSchema(BaseModel):
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
    budget: Optional[int]
    revenue: Optional[int]
    country: str

    class Config:
        orm_mode = True  # важливо для SQLAlchemy об'єктів


# Схема для списку фільмів із пагінацією
class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int

import datetime
from typing import List, Optional
from pydantic import BaseModel


class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: Optional[datetime.date]
    score: Optional[int]
    genre: Optional[str]
    overview: Optional[str]
    crew: Optional[str]
    orig_title: Optional[str]
    status: Optional[str]
    orig_lang: Optional[str]
    budget: Optional[int]
    revenue: Optional[int]
    country: Optional[str]

    class Config:
        orm_mode = True


class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int

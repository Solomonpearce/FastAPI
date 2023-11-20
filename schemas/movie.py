from pydantic import BaseModel,Field  # para validar los datos que se envian
from typing import Optional # para validar los datos que se envian

#Esquema de pydantic para validar los datos que se envian
class Movie(BaseModel):
    id: Optional[int] = None
    title: str=Field(min_length=2,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int=Field(le=2023,ge=1920)
    rating: float = Field(le=10,ge=0)
    category: str=Field(min_length=5,max_length=50)
    class Config:
        json_schema_extra = { #Para valores por defecto y ya se llama json_schema_extra
            "example": {
                "id": 1,
                "title": "Example Movie",
                "overview": "A short description",
                "year": 2023,
                "rating": 8.5,
                "category": "Action | Adventure | Sci-Fi"
            }
        }


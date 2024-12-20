from pydantic import BaseModel
from typing import Optional
import datetime

# user
class UserCreate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: str
    number: str
    brith_day: Optional[datetime.date]

class UserUpdate(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[str]
    brith_day: Optional[datetime.date]

class UserResult(BaseModel):
    name: Optional[str]
    email: Optional[str]
    number: Optional[str]
    brith_day: Optional[datetime.date]

# product
class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    futures: dict
    subcategory_name: str # arrive the name then I find it is id from it

class ProductUpdate(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]
    futures: Optional[dict]
    subcategory_name: Optional[str]

class ProductResult(BaseModel):
    name: str
    description: str
    price: int
    futures: dict
    comments: Optional[list]


# subcategory
class SubcategoryCreate(BaseModel):
    name: str
    category_name: str # arrive the name then I find it is id from it

class SubcategoryUpdate(BaseModel):
    id: int
    name: Optional[str]
    category_name: Optional[str]

class SubcategoryResult(BaseModel):
    name: str
    products: Optional[list[ProductResult]]

# category
class CategoryCreate(BaseModel):
    name: str

class CategoryUpdate(BaseModel):
    id: int
    name: str

class CategoryResult(BaseModel):
    name: str
    subcategories: Optional[list[SubcategoryResult]]

# Commentary
class CommentCreate(BaseModel):
    writer_name: str
    star: int
    like: int
    unlike: int
    product_id: int

class CommentUpdate(BaseModel):
    id: int
    star: int
    like: int
    unlike: int

class CommentResult(BaseModel):
    writer_name: str
    star: int
    like: int
    unlike: int
    date: datetime.datetime

# Location
class LocationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    user_id: int

class LocationUpdate(BaseModel):
    id: int
    name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]

class LocationResult(BaseModel):
    name: str
    latitude: float
    longitude: float
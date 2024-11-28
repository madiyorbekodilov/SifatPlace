from sqlalchemy import create_engine, Column, Integer, String, DATE, JSON, ForeignKey, Boolean, DATETIME, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Relationship

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:194853@localhost:5432/SifatTest"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    number = Column(String)
    brith_day = Column(DATE)

    location = Relationship("Location", back_populates="users")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    futures = Column(JSON)
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))

    subcategory = relationship("SubCategory", back_populates="products")
    comment = relationship("Comment", back_populates="product")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    subcategories = relationship("SubCategory", back_populates="category")

class SubCategory(Base):
    __tablename__ = "subcategories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="subcategories")
    products = relationship("Product", back_populates="subcategory")


class ProductPhoto(Base):
    __tablename__ = "productphotos"
    id = Column(Integer, primary_key=True)
    color = Column(String)
    is_have = Column(Boolean)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="photos")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    writer_name = Column(String)
    star = Column(Integer)
    date = Column(DATETIME)
    like = Column(Integer)
    unlike = Column(Integer)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="comments")


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="locations")
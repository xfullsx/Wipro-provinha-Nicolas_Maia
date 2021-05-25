from sqlalchemy import String, Column, Integer, Boolean
from pydantic import BaseModel
from repository.repository import Base


class ResidenceModel(Base):
    __tablename__ = "residence".upper()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True)
    host_id = Column(String(100), index=True)
    host_name = Column(String(100))
    neighbourhood_group = Column(String(100))
    neighbourhood = Column(String(100))
    latitude = Column(String(100))
    longitude = Column(String(100))
    room_type = Column(String(100))
    price = Column(String(100))
    minimum_nights = Column(String(100))
    number_of_reviews = Column(String(100))
    last_review = Column(String(100))
    reviews_per_month = Column(String(100))
    calculated_host_listings_count = Column(String(100))
    availability_365 = Column(String(100))


class ResidenceModelLike(Base):
    __tablename__ = "residence_like".upper()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    like = Column(Boolean())


class ModelLike(BaseModel):
    id: int
    like: bool

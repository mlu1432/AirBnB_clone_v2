#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel

class Place(BaseModel):
    """ A place to stay """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = None
    longitude: float = None
    amenity_ids: list = None

    def __init__(self, *args, **kwargs):
        """Initialize a new Place."""
        super().__init__(*args, **kwargs)
        if self.amenity_ids is None:
            self.amenity_ids = []
        self.validate_attributes()

    def validate_attributes(self):
        """Validate attributes to ensure data integrity."""
        if not isinstance(self.number_rooms, int) or self.number_rooms < 0:
            raise ValueError("number_rooms must be a non-negative integer")
        if not isinstance(self.number_bathrooms, int) or self.number_bathrooms < 0:
            raise ValueError("number_bathrooms must be a non-negative integer")
        if not isinstance(self.max_guest, int) or self.max_guest < 0:
            raise ValueError("max_guest must be a non-negative integer")
        if not isinstance(self.price_by_night, int) or self.price_by_night < 0:
            raise ValueError("price_by_night must be a non-negative integer")
        if self.latitude is not None and (self.latitude < -90 or self.latitude > 90):
            raise ValueError("latitude must be between -90 and 90")
        if self.longitude is not None and (self.longitude < -180 or self.longitude > 180):
            raise ValueError("longitude must be between -180 and 180")
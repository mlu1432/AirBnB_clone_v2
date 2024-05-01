#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel

class City(BaseModel):
    """ Representation of a City """
    state_id = ""  # Will store the id of the State
    name = ""

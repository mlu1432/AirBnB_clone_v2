#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        
        # Convert strings to datetime if necessary
        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.created_at = datetime.now()

        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.updated_at = datetime.now()

        # Remove class key if it's in kwargs to avoid conflicts with actual attributes
        kwargs.pop('__class__', None)
        # Additional attributes from kwargs
        self.__dict__.update(kwargs)

        # Store the object in storage if not loading from storage
        if not kwargs:
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = type(self).__name__
        return f'[{cls_name}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = type(self).__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

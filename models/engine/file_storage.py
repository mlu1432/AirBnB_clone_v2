#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects, or all objects of a class if specified."""
        if cls:
            class_name = cls.__name__
            filtered_dict = {k: v for k, v in FileStorage.__objects.items() if k.startswith(class_name)}
            return filtered_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                cls_name = val['__class__']
                if cls_name in classes:
                    self.__objects[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

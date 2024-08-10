#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def get(self, cls, id):
        """A method to retrieve an object"""
        objects_class = self.all()
        for obj in object_class.values():
            if id == str(obj.id):
                return obj
            else:
                return None

    def count(self, cls=None):
        """The count of objects"""
        if cls is not None:
            return len(self.all(cls))
        else:
            return len(self.all())

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

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
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Deletes an object"""
        if obj is None:
            return
        for obj_class in FileStorage.__object.keys():
            if obj.id == obj_class.split(".")[1] and obj_class.split(".")[0] in str(obj)
            FileStorage.__object.pop(obj_class)
            self.save()

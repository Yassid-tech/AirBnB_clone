#!/usr/bin/python3
""" Define the FileStorage class. """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Represent an abstracted storage engine.
       Attributes:
          __file_path (str): The name of the file to save objects to.
          __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path """
        ydict = FileStorage.__objects
        objdict = {obj: ydict[obj].to_dict() for obj in ydict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ Deseroalize the JSON file __file_path to __objects,
            if it exists. """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for y in objdict.values():
                    cl_name = y["__class__"]
                    del y["__class__"]
                    self.new(eval(cl_name)(**y))
        except FileNotFoundError:
            return

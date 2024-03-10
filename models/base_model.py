#!/usr/bin/python3
""" Module: base.py """
import models
import uuid
from datetime import datetime


class BaseModel:
    """ Base class wich defines all common attributes,
        methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initiation of an object
            with it's attributes.
            Args:
                 *args (any): Unused.
                 **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
                setattr(self, key, value)

        else:
            models.storage.new(self)

    def __str__(self):
        """ Returns the string representation of the instance
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(
            clname, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
            of __dict__ of the instance.
        """
        ydict = self.__dict__.copy()
        ydict['__class__'] = self.__class__.__name__
        ydict['created_at'] = ydict['created_at'].isoformat()
        ydict['updated_at'] = ydict['updated_at'].isoformat()

        return ydict

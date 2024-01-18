#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the current object.

        This method updates the `updated_at` attribute of the object to the current datetime in UTC.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        :return: A dictionary containing the object's attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "1st model"
    my_model.nmbr = 46
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my model: ")
    for key in my_model_json.keys():
        print(
            "\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key])
        )

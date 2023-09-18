#!/usr/bin/python3

import json
import csv
import turtle

class Base:
    """Base class for managing object IDs and serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The unique identifier for the object. If None, it will be generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be serialized and saved to a JSON file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from a dictionary representation.

        Args:
            dictionary (dict): Dictionary containing object attributes and their values.

        Returns:
            Base: An instance of the class.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file and return a list of instances.

        Returns:
            list: List of instances created from the data in the JSON file.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to be serialized and saved to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file and return a list of instances.

        Returns:
            list: List of instances created from the data in the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using the Turtle graphics library.

        Args:
            list_rectangles (list): List of Rectangle objects to be drawn.
            list_squares (list): List of Square objects to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.color("#ffffff")
        turt.shape("turtle")
        turt.pensize(2)

        for rect in list_rectangles:
            turt.penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.penup()

        for square in list_squares:
            turt.penup()
            turt.goto(square.x, square.y)
            turt.pendown()
            for _ in range(4):
                turt.forward(square.size)
                turt.left(90)
            turt.penup()

        turtle.done()
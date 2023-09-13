#!/usr/bin/python3
"""A representation of class student"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - to_json(self): Retrieves a dictionary representation of
    a Student instance.

    Example:
    >>> student = Student("John", "Doe", 23)
    >>> student_dict = student.to_json()
    >>> print(type(student_dict))
    <class 'dict'>
    >>> print(student_dict['first_name'])
    'John'
    >>> print(type(student_dict['first_name']))
    <class 'str'>
    >>> print(student_dict['age'])
    23
    >>> print(type(student_dict['age']))
    <class 'int'>
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__

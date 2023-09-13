#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - to_json(self, attrs=None): Retrieves a dictionary representation
    of a Student instance.

    If 'attrs' is a list of strings, only the attribute names
    contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved.

    Example:
    >>> student_1 = Student("John", "Doe", 23)
    >>> student_2 = Student("Bob", "Dylan", 27)

    >>> j_student_1 = student_1.to_json()
    >>> j_student_2 = student_2.to_json(['first_name', 'age'])
    >>> j_student_3 = student_2.to_json(['middle_name', 'age'])

    >>> print(j_student_1)
    {'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
    >>> print(j_student_2)
    {'age': 27, 'first_name': 'Bob'}
    >>> print(j_student_3)
    {'age': 27}
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If 'attrs' is a list of strings, only the attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if (type(attrs) is list and
                all(type(attribute) is str for attribute in attrs)):
            return {attribute: getattr(self, attribute) for attribute in attrs if hasattr(self, attribute)}
        return self.__dict__

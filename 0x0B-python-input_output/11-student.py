#!/usr/bin/python3
"""This class Student that defines a student(based on 10-student.py)"""


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
      If 'attrs' is a list of strings, only attribute names contained
      in this list must be retrieved.
      Otherwise, all attributes must be retrieved.

    - reload_from_json(self, json): Replaces all attributes of the
    Student instance using a provided dictionary.
      The keys in the dictionary are used as attribute names, and the
      values as attribute values.

    Example:
    >>> student_1 = Student("John", "Doe", 23)
    >>> j_student_1 = student_1.to_json()
    >>> print(student_1)
    <Student object at ...>
    >>> print(type(student_1))
    <class 'Student'>
    >>> print(type(j_student_1))
    <class 'dict'>
    >>> print("{} {} {}".format(student_1.first_name,
        student_1.last_name, student_1.age))
    John Doe 23

    >>> save_to_json_file(j_student_1, "student.json")
    >>> read_file("student.json")

    >>> new_student_1 = Student("Fake", "Fake", 89)
    >>> print(new_student_1)
    <Student object at ...>
    >>> print(type(new_student_1))
    <class 'Student'>
    >>> print("{} {} {}".format(new_student_1.first_name,
        new_student_1.last_name, new_student_1.age))
    Fake Fake 89

    >>> new_j_student_1 = load_from_json_file("student.json")
    >>> new_student_1.reload_from_json(j_student_1)
    >>> print(new_student_1)
    <Student object at ...>
    >>> print(type(new_student_1))
    <class 'Student'>
    >>> print("{} {} {}".format(new_student_1.first_name,
        new_student_1.last_name, new_student_1.age))
    John Doe 23
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If 'attrs' is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if (type(attrs) is list and
                all(type(attribute) is str for attribute in attrs)):
            return {attribute: getattr(self, attribute) for attribute in attrs if hasattr(self, attribute)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using
        a provided dictionary.

        The keys in the dictionary are used as attribute names,
        and the values as attribute values.
        """
        for attribute, value in json.items():
            setattr(self, attribute, value)

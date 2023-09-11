#!/usr/bin/python3
""" This class MyList that inherits from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the elements of the list in sorted (ascending) order.

        Args:
            None

        Returns:
            None

        Example:
            my_list = MyList()
            my_list.append(1)
            my_list.append(4)
            my_list.append(2)
            my_list.append(3)
            my_list.append(5)
            print(my_list)          # Output: [1, 4, 2, 3, 5]
            my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
            print(my_list)          # Output: [1, 4, 2, 3, 5]
        """
        print(sorted(self))

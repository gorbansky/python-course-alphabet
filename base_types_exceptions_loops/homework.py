import string

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    print('BONJORNO! I`m exception!')


def is_two_object_has_same_value(first: Any, second: Any) -> bool:

    """
    If @first and @second has same value should return True
    In another case should return False
    """

    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:

    """
    If @first and @second has same type should return True
    In another case should return False
    """

    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:

    """
    If @first and @second has same object should return True
    In another case should return False
    """

    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:

    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """

    if not isinstance(first_value, int) or not isinstance(second_value, int):
        raise ValueError
    else:
        return first_value * second_value


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:

    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """

    try:
        return int(first_value) * int(second_value)
    except ValueError:
        raise OurAwesomeException
    pass


def is_word_in_text(word: str, text: str) -> bool:

    """
       If text contain word return True
       In another case return False.

       Args:
           word: Searchable substring
           text: Text for searching

       Examples:
           is_word_in_text("Hello", "Hello word")
           >>> True
           is_word_in_text("Glad", "Nice to meet you ")
           >>> False

       """

    return word in text


def some_loop_exercise() -> list:

    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """

    v_list = []
    for num in range(13):
        if num not in (6, 7):
            v_list.append(num)
    return v_list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:

    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """

    v_list = []
    for num in data:
        if num >= 0:
            v_list.append(num)
    return v_list


def alphabet() -> dict:

    """
    Create dict which keys is number in alphabet
    And values their alphabetic characters.
    Notes You could see an implementaion of this one in test,
    but create another one
    Examples:
        alphabet()
        >>> {1: "a", 2: "b" ...}
    """

    v_dict = {}
    for count, char in enumerate(string.ascii_lowercase, 1):
        v_dict[count] = char
    return v_dict


def simple_sort(data: List[int]) -> List[list]:

    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """

    for v_loop_1 in range(len(data)):
        for v_loop_2 in range(v_loop_1 + 1, len(data)):
            if data[v_loop_1] > data[v_loop_2]:
                data[v_loop_1], data[v_loop_2] = data[v_loop_2], data[v_loop_1]
    return (data)

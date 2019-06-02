import random

from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """

    def make_title(p_dict: dict) -> dict:
        if 'name' in p_dict:
            p_dict['name'] = p_dict['name'].title()
        return p_dict
    return list(map(make_title, data))


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """

    def del_key(p_dict: dict) -> dict:
        for v_key in redundant_keys:
            del p_dict[v_key]
        return p_dict
    return list(map(del_key, data))


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """

    return list(filter(lambda v_dict: value in v_dict.values(), data))


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """

    return min(data, default=None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """

    return min(map(str, data), key=len, default=None)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """

    return min(filter(lambda v_dict: key in v_dict, data), key=lambda v_dict: v_dict[key])


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """

    return max([v_num for v_list in data for v_num in v_list], default=None)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """

    return sum(map(lambda x: x, data))


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """

    return sum(map(lambda x: ord(x), text))


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """

    def is_prime(value):
        for i in range(3, value, 2):
            if value % i == 0:
                return False
        return True

    yield 2
    for i in range(3, 200, 2):
        v_out = i
        if is_prime(v_out):
            yield v_out


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each
    element is random letter from latin alphabet

    """

    return [chr(random.randint(97, 122)) for i in range(20)]

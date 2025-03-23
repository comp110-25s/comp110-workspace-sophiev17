"makin' a dictionary for exercise 3!"

__author__ = "730579326"


def invert(switch: dict[str, str]) -> dict[str, str]:
    """Goal is to invert the key and values for each dictionary entry"""
    inverted_dict: dict[str, str] = {}
    all_keys: list[str] = []
    idx: int = 0

    """Key values in the switch dictionary will be added to a list called all_keys"""
    for key in switch:
        all_keys.append(key)

    """While the index is less than the number of keys in the original dictionary, the key and value switch"""
    while idx < len(all_keys):
        """The key at that particular index from the listt of keys becomes the new value of the key variable as the loop progresses"""
        key = all_keys[idx]
        """This pulls the corresponding value for the original key and value pair in the original dictionary"""
        value = switch[key]
        """This loop only continues if there isn't already """
        if value in inverted_dict:
            raise KeyError(
                f"Duplicate found of '{value}'. Retry using dictionary with all uniques values"
            )
        """This makes a new dictionary where the keys and values from the original dictionary switch and adds to the dictionary with each iteration of the while loop"""
        inverted_dict[value] = key
        """This increases the index so an infinite loop isn't created"""
        idx += 1

    return inverted_dict


def count(list: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(list):
        item = list[idx]
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
        idx += 1
    return new_dict


def favorite_color(namescolors: dict[str, str]) -> str:
    all_colors: list[str] = []
    idx: int = 0
    max_color: str
    max_count: int = 0

    """Names in the namescolors dictionary will be added to a list called all_colors"""
    for key in namescolors:
        all_colors.append(namescolors[key])
    color_count = count(all_colors)

    while idx < len(all_colors):
        color = all_colors[idx]
        count = color_count[color]
        if count > max_count:
            max_color = color
            max_count = count
        idx += 1
    return max_color

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

    while idx < len(all_keys):
        """Key at that index becomes new value"""
        key = all_keys[idx]
        """Pulls corresponding value for og key and value pair in og dictionary"""
        value = switch[key]
        """This loop only continues if there isn't already """
        if value in inverted_dict:
            raise KeyError(
                f"Duplicate found of '{value}'. Retry using all uniques values"
            )
        """New dictionary, keys and values switch and adds to dict with each loop"""
        inverted_dict[value] = key
        idx += 1

    return inverted_dict


def count(list: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    idx: int = 0
    """Associates items with the number of times they occurred in the string"""
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
    count(all_colors)
    color_count = count(all_colors)
    """Loops through each color"""
    while idx < len(all_colors):
        color = all_colors[idx]
        ongoing_count = color_count[color]
        """If this color's count is higher than the current max then update"""
        if ongoing_count > max_count:
            max_color = color
            max_count = ongoing_count
        idx += 1
    return max_color


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    bin_dict: dict[int, set[str]] = {}

    for string in bins:
        length = len(string)

        if length in bin_dict:
            bin_dict[length].add(string)
        else:
            bin_dict[length] = {string}
    return bin_dict

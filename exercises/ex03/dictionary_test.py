"""Testin' my functions for exercise 3!"""

__author__ = "730579326"

from exercises.ex03.dictionary import invert


def test_invert_use1() -> None:
    """Test use case for invert function with dogs and their names"""
    assert invert({"Golden Retriever": "Buddy", "Corgi": "Elizabeth"}) == {
        "Buddy": "Golden Retriever",
        "Elizabeth": "Corgi",
    }


def test_invert_use2() -> None:
    """Test Use case with letters for invert"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_edgecase() -> None:
    """Test edge case for invert"""
    assert invert({}) == {}


import pytest


def test_invert_KeyError() -> None:
    """Test KeyError is working for invert"""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


from exercises.ex03.dictionary import count


def test_count_use1() -> None:
    """Test use case for count"""
    assert count(["apple", "banana", "apple", "apple"]) == {"apple": 3, "banana": 1}


def test_count_use2() -> None:
    """Test use case for count again"""
    assert count(["1", "2", "3", "4", "5"]) == {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}


def test_count_edgecase() -> None:
    """Test edgecase for count"""
    assert count(["dog"]) == {"dog": 1}


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_use1() -> None:
    """test use case for favorite color"""
    assert favorite_color({"Joe": "green", "Bob": "blue", "Jane": "green"}) == "green"


def test_favorite_color_use2() -> None:
    """test use case for favorite color again"""
    assert (
        favorite_color(
            {"Bill": "purple", "Casey": "blue", "Morgan": "black", "Val": "purple"}
        )
        == "purple"
    )


def test_favorite_color_edgecase() -> None:
    """Test edgecase for favorite color"""
    assert (
        favorite_color(
            {
                "Jen": "lilac",
                "Zach": "emerald",
                "Micahel": "azure",
                "Leslie": "azure",
                "Caroline": "maroon",
                "Silas": "maroon",
            }
        )
        == "azure"
    )


from exercises.ex03.dictionary import bin_len


def test_bin_len_use1() -> None:
    """Test use case for bin length function"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2() -> None:
    """Test use case for bin length function again"""
    assert bin_len(["wow", "she", "is", "coding"]) == {
        3: {"wow", "she"},
        2: {"is"},
        6: {"coding"},
    }


def test_bin_len_edgecase() -> None:
    """Test edge case for bin length function"""
    assert bin_len({}) == {}

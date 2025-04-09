"""This file runs the river simulation from the fish, bear and river classes"""

__author__ = "730579326"

from exercises.EX04.river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()
my_river.one_river_week()

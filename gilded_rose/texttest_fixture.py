# -*- coding: utf-8 -*-

from modules.gilded_rose import GildedRose
from utils.main_helper import prep_items
import argparse

parser = argparse.ArgumentParser(
    description=
    "This program calculates items quality and sellIn date given a number of days."
)
parser.add_argument(
    '-d',
    '--days',
    dest='days',
    help=
    'Number of days for which the quality and sellIn date will be calculated.',
    default=2,
    type=int)
parser.add_argument(
    '-ip',
    '--items-path',
    dest='items_path',
    help=
    'the path to a JSON file which has items you want to calculate the quality for.',
    default="items/items.json",
    type=str)
args = parser.parse_args()


def main():
    '''Iterates through items of different categories and updates their quality.'''
    items = prep_items(args.items_path)
    for day in range(args.days + 1):
        print("\n-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()

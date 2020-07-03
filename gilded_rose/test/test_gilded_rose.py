# -*- coding: utf-8 -*-
import unittest

from modules.item_categories import *
from modules.gilded_rose import GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_general_sellin_positive(self):
        items = [
            GeneralItem(name="Elixir of the Mongoose", sell_in=5, quality=7)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 4, 6

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_general_sellin_negative(self):
        items = [
            GeneralItem(name="Elixir of the Mongoose", sell_in=-2, quality=5)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = -3, 3

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_general_quality_under_0(self):
        items = [
            GeneralItem(name="Elixir of the Mongoose", sell_in=1, quality=0)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 0, 0

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_aged_brie_sellin_positive(self):
        items = [AgedBrie(name="Aged Brie", sell_in=2, quality=0)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 1, 1

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_aged_brie_sellin_negative(self):
        items = [AgedBrie(name="Aged Brie", sell_in=0, quality=2)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = -1, 4

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_aged_brie_quality_above_50(self):
        items = [AgedBrie(name="Aged Brie", sell_in=4, quality=50)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 3, 50

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_sulfuras_sellin_0(self):
        items = [
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 0, 80

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_sulfuras_sellin_negative(self):
        items = [
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = -1, 80

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_backstage_passes_sellin_above_10(self):
        items = [
            BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert",
                            sell_in=15,
                            quality=20)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 14, 21

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_backstage_passes_sellin_between_6_and_10(self):
        items = [
            BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert",
                            sell_in=7,
                            quality=35)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 6, 37

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_backstage_passes_sellin_between_1_and_5(self):
        items = [
            BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert",
                            sell_in=2,
                            quality=35)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 1, 38

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_backstage_passes_quality_drop_0(self):
        items = [
            BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert",
                            sell_in=0,
                            quality=30)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = -1, 0

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_backstage_passes_quality_above_50(self):
        items = [
            BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert",
                            sell_in=7,
                            quality=50)
        ]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 6, 50

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_conjured_sellin_positive(self):
        items = [Conjured(name="Conjured Mana Cake", sell_in=5, quality=7)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 4, 5

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_conjured_sellin_negative(self):
        items = [Conjured(name="Conjured Mana Cake", sell_in=-2, quality=5)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = -3, 1

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)

    def test_conjured_quality_under_0(self):
        items = [Conjured(name="Conjured Mana Cake", sell_in=1, quality=0)]
        GildedRose(items).update_quality()
        sell_in_result, quality_result = items[0].sell_in, items[0].quality
        sell_in_expected, quality_expected = 0, 0

        self.assertEqual(sell_in_result, sell_in_expected)
        self.assertEqual(quality_result, quality_expected)


if __name__ == '__main__':
    unittest.main()
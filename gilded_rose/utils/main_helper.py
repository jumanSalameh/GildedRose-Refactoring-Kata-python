from modules.item_categories import *
import json


def prep_items(path_to_items):
    """retuens a list of Item types from a json file.

    Parameters:
    path_to_items (str): Path to json file containing items

    Returns:
    items: List of item types

    """
    items = []
    with open(path_to_items, "r") as items_file:
        items_json = json.load(items_file)
        for item in items_json['items']:
            if item["category"] == "Backstage passes":
                items.append(
                    BackstagePasses(name=item["name"],
                                    sell_in=item["sell_in"],
                                    quality=item["quality"]))
            elif item["category"] == "Aged Brie":
                items.append(
                    AgedBrie(name=item["name"],
                             sell_in=item["sell_in"],
                             quality=item["quality"]))
            elif item["category"] == "Sulfuras":
                items.append(
                    Sulfuras(name=item["name"],
                             sell_in=item["sell_in"],
                             quality=item["quality"]))
            elif item["category"] == "Conjured":
                items.append(
                    Conjured(name=item["name"],
                             sell_in=item["sell_in"],
                             quality=item["quality"]))
            else:
                items.append(
                    GeneralItem(name=item["name"],
                                sell_in=item["sell_in"],
                                quality=item["quality"]))
    return items
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GeneralItem(Item):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2

        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1


class AgedBrie(GeneralItem):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality += 1
        else:
            self.quality += 2

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1


class BackstagePasses(GeneralItem):
    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif 6 <= self.sell_in <= 10:
            self.quality += 2
        elif 1 <= self.sell_in <= 5:
            self.quality += 3
        else:
            self.quality = 0

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1


class Sulfuras(GeneralItem):
    def update_quality(self):
        pass


class Conjured(GeneralItem):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 2
        else:
            self.quality -= 4

        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1
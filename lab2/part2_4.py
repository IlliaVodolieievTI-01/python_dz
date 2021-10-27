class Tree:
    def __init__(self, key, price):
        self.__key = key
        self.__price = price
        self.left = None
        self.right = None

    @property
    def key(self):
        return self.__key

    @property
    def price(self):
        return self.__price

    @key.setter
    def key(self, elem):
        if isinstance(elem, int):
            self.__key = elem
        else:
            raise TypeError("Key must be integer!")

    @price.setter
    def price(self, elem):
        if isinstance(elem, (int, float)):
            self.__price = elem
        else:
            raise TypeError("Price must be integer or float!")

    def add(self, key, price):
        if self.key:
            if self.left is None:
                self.left = Tree(key, price)
            else:
                self.left.add(key, price)

                if self.right is None:
                    self.right = Tree(key, price)
                else:
                    self.right.add(key, price)
        else:
            self.key = key
        return self.key

    def find(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Value must be integer!")
        else:
            if key < self.key:
                if self.left is None:
                    return None
                return self.left.find(key, value)
            elif key > self.key:
                if self.right is None:
                    return None
                return self.right.find(key, value)
            else:
                return self.price * value

def main():
    firsttree = Tree(12, 10)
    firsttree.add(7, 2)
    firsttree.add(13, 15)
    firsttree.add(20, 4)
    firsttree.add(24, 7)
    firsttree.add(14, 17)
    firsttree.add(3, 21)
    print(firsttree.find(3, 10))
    print(firsttree.find(7, 2))
    print(firsttree.find(34, 2))


main()
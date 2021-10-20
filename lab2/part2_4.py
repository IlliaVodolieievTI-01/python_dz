class Tree:
    def __init__(self, key, price):
        self.key = key
        self.price = price
        self.left = None
        self.right = None

    def add(self, key, price):
        if not isinstance(key, int):
            raise TypeError("Key must be integer!")
        else:
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
            return (self.key)

    def find(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Value must be integer!")
        else:
            if key < self.key:
                if self.left is None:
                    return str(key)+" Not Found"
                return self.left.find(key, value)
            elif key > self.key:
                if self.right is None:
                    return str(key)+" Not Found"
                return self.right.find(key, value)
            else:
                return self.price * value
    def back(self):
        self.left = None
        self.right = None

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


if __name__ == '__main__':
    main()
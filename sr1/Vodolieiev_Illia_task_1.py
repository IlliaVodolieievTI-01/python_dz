#I did this task at the end and was in a hurry, but decided to send what I have
class Tree:
    def __init__(self, name, author, year, edition):
        if isinstance(name, str):
            self.__name = name
        raise TypeError("Wrong type!")
        if isinstance(author, str):
            self.__author = author
        raise TypeError("Wrong type!")
        if isinstance(year, str):
            self.__year = year
        raise TypeError("Wrong type!")
        if isinstance(edition, str):
            self.__edition = edition
        raise TypeError("Wrong type!")
        self.left = None
        self.right = None


    def add(self, name, author, year, edition):
        if self.__name:
            if self.left is None:
                self.left = Tree(name, author, year, edition)
            else:
                self.left.add(name, author, year, edition)

                if self.right is None:
                    self.right = Tree(name, author, year, edition)
                else:
                    self.right.add(name, author, year, edition)
        else:
            self.__name = name
        return self.__name

    def find_name(self, name):
        if self.left is None:
            return None
        return self.left.find_name(name)
        if self.right is None:
            return None
        return self.right.find_name(name)
        return f"{self.__name} {self.__author} {self.__year} {self.__edition}"

    def find_author(self, author):
        if self.left is None:
            return None
        return self.left.find_author(author)
        if self.right is None:
            return None
        return self.right.find_author(author)
        return f"{self.__name} {self.__author} {self.__year} {self.__edition}"


firsttree = Tree("Harry Potter", "Rowling", 2011, "Children's Fiction")
firsttree.add("Twilight", "Meyer", 2008, "Young Adult Fiction")
firsttree.add("New Moon", "Meyer", 2012, "Young Adult Fiction")
firsttree.add("Digital Fortress", "Brown", 2017, "Crime, Thriller & Adventure")
print(firsttree.find_name("Harry Potter"))
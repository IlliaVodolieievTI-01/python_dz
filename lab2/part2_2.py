import re
class Files:
    def __init__(self):
        self.words = 0
        self.characters = 0
        self.__content = ""
    

    def get_words(self, name):
        file = open(name)
        for line in file:
            wordslist = line.split()
            self.words = self.words + len(wordslist)
        file.close()
        return self.words

    def get_characters(self, name):
        file = open(name)
        for line in file:
            self.characters = self.characters + len(line)
        file.close()
        return self.characters

    def get_sentences(self, name):
        sentences = 0
        with open(name) as file:
            for line in file:
                sentences += len(re.split(r"[.!?]+", line))
            if not line.endswith('.' or '!' or '?'):
                    sentences -= 1
        return sentences


firstfile = Files()
print("Num of words in your file: ")
print(firstfile.get_words('1.txt'))
print("Num of characters in your file: ")
print(firstfile.get_characters('1.txt'))
print("Num of sentences in your file: ")
print(firstfile.get_sentences('1.txt'))
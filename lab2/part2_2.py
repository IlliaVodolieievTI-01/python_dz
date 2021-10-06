class Files:
    def __init__(self):
        self.words = 0;
        self.characters = 0;
    

    def get_words(self):
        file = open('1.txt')
        for line in file:
            wordslist = line.split()
            self.words = self.words + len(wordslist)
        file.close()
        return self.words

    def get_characters(self):
        file = open('1.txt')
        for line in file:
            self.characters = self.characters + len(line)
        file.close()
        return self.characters


firstfile = Files()
print("Num of words in your file: ")
print(firstfile.get_words())
print("Num of characters in your file: ")
print(firstfile.get_characters())
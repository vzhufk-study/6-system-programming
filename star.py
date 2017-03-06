# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 27.02.2017

Asterisk = "*"


class AsteriskPattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.split = pattern.split(Asterisk)
        self.text = ""
        self.result = []

    def init(self, pattern):
        self.pattern = pattern
        self.split = pattern.split(Asterisk)

    def check(self, word):
        """
        Checks if word is similar to pattern
        :param word: string
        :return: bool of similarity
        """
        # If first is not asterisk
        if self.split[0] != '' and word.find(self.split[0]) != 0:
            return False
        else:
            # current var here is for faster and correct find function
            current = 0
            for i in range(0, len(self.split)):
                current = word.find(self.split[i], current)
                if current < 0:
                    return False
                current += len(self.split[i])

            if self.split[i] != '' and self.split[i] != word[len(word) - len(self.split[i]):]:
                return False
            else:
                return True

    def file(self, filename):
        file = open(filename, "r+")
        text = file.read()
        self.init(text.split("\n")[0])
        result = []
        # Split and check
        self.text = text.split("\n")[1]
        for i in self.text.split(" "):
            if self.check(i):
                result.append(i)
        file.close()

        self.result = []
        self.result.append(result)
        result.sort(key=len, reverse=False)
        self.result.append(result)
        # Open same file
        file = open(filename, "a+")
        file.write(str(self.result[0]) + "\n")
        file.write(str(self.result[1]) + "\n")


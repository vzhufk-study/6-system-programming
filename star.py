# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 27.02.2017

Asterisk = "*"


class AsteriskPattern:
    def __init__(self, pattern):
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
            for i in range(0, len(self.split) - 1):
                current = word.find(self.split[i], current)
                if current < 0:
                    return False
                current += len(self.split[i])

            # If Last is not asterisk
            i = len(self.split) - 1
            if self.split[i] != '' and self.split[i] != word[len(word) - len(self.split[i]):]:
                return False
            else:
                return True
'''
x = AsteriskPattern(input("Set pattern:"))
print(x.check(input("Set word:")))
'''
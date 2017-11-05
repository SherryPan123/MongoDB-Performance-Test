class Comment:
    list1 = []

    def addPair(self, key, value):
        self.list1.append(key)
        self.list1.append(value)

    def printComment(self):
        i = 0
        while i < len(self.list1):
            if i % 2 == 0:
                print(self.list1[i]+': ', end="")
            if i % 2 == 1:
                print(self.list1[i])
            i += 1
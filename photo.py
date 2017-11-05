class Photo:
    # extracted from exif
    list1 = []
    owner = None
    usedCamera = None
    comment = None

    def addPair(self, key, value):
        self.list1.append(key)
        self.list1.append(value)

    def setOwner(self, _owner):
        self.owner = _owner

    def setCamera(self, _camera):
        self.usedCamera = _camera

    def setComment(self, _comment):
        self.comment = _comment

    def printPhoto(self):
        print('[photo]')
        i = 0
        while i < len(self.list1):
            if i % 2 == 0:
                print(self.list1[i] + ': ', end="")
            if i % 2 == 1:
                print(self.list1[i])
            i += 1

        print('[owner]')
        self.owner.printUser()
        print('[camera]')
        self.usedCamera.printCamera()
        print('[comment]')
        self.comment.printComment()
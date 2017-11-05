class Camera:
    'Name of camera'
    name = ''

    def __init__(self, name):
        self.name = name

    def printCamera(self):
        print(self.name)
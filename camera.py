class Camera:
    'Name of camera'
    name = ''
    type = ''

    def addMake(self, Make):
        self.name = Make

    def addModel(self, Model):
        self.type = Model

    def printCamera(self):
        print('Make: '+self.name)
        print('Model: '+self.type)
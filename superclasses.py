from abc import abstractmethod
class Bird:
    def __init__(self,name):
        self.name = name
    fly = True

    def noise(self):
        print("birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass
    extinct = False

class Owl(Bird):
    def __init__(self, name, age):
        super(Owl, self).__init__(name)
        self.age = age

    def reproduce(self):
        self.babies += 6
    
    def eat(self):
        print("Peck Peck")

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        print("Nom Nom")
    
    def reproduce(self):
        if extinct == False:
            self.babies += 1
        else:
            print("No more dodos")

owl1 = Owl("Geoff", 10)

owl1.reproduce()
print(owl1.babies)
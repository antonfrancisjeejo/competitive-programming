class Animal:
    def __init__(self):
        self.cat = []
        self.dog = []
        self.any = []
        self.animals = []

    def cats(self):
        self.cat.append(1)
        self.any.append(1)

    def dogs(self):
        self.dog.append(2)
        self.any.append(2)

    def enqueue(self):
        while self.any:
            self.animals.append(self.any.pop())

    def printe(self):
        print(self.animals)

    def dequeue_any(self):
        x = self.animals[0]
        self.animals.remove(x)
        if x == 1:
            self.cat.pop()
        else:
            self.dog.pop()

    def dequeue_cat(self):
        self.cat.pop()
        self.animals.remove(1)

    def dequeue_dog(self):
        self.dog.pop()
        self.animals.remove(2)

    def print_no_dogs(self):
        if len(self.dog) > 0:
            print(len(self.dog))
        else:
            print('No more dogs')

    def print_no_cats(self):
        if len(self.cat) > 0:
            print(len(self.cat))
        else:
            print('No more cats')


s = Animal()
s.cats()
s.dogs()
s.dogs()
s.cats()
s.dogs()
s.dogs()
s.cats()
s.enqueue()
s.dequeue_any()
s.dequeue_cat()
s.dequeue_cat()
s.dequeue_any()
s.printe()
s.print_no_cats()
s.print_no_dogs()



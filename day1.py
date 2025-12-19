

def rotate_right(position, rotation):
    return (position + rotation) % 100

def rotate_left(position, rotation):
    return (position - rotation) % 100

class Dial:

    def __init__(self):
        self.position = 50
        self.password = 0

    def increment(self):
        self.position += 1
        self.position = self.position % 100
        if self.position == 0:
            self.password += 1

    def decrement(self):
        self.position -= 1
        self.position = self.position % 100
        if self.position == 0:
            self.password += 1

    def rotate_left(self, rotation):
        for i in range(rotation):
            self.decrement()

    def rotate_right(self, rotation):
        for i in range(rotation):
            self.increment()


dial = Dial()
with open('input1.txt') as file:
    for line in file:
        rotation_type = line[0]
        rotation = int(line[1:])
        if rotation_type == "L":
            position = dial.rotate_left(rotation)
        if rotation_type == "R":
            position = dial.rotate_right(rotation)


print(f"Password is {dial.password}")
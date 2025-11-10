class Mathematics:
    def __init__(self):
        self.number = input("Enter numbers separated by space: ").split()

    def addition(self):
        total = 0
        for i in self.number:
            total += int(i)
        print("Sum:", total)

    def substraction(self):
        total = int(self.number[0])
        for i in self.number[1:]:
            total -= int(i)
        print("Substraction:",total)

a = Mathematics()
a.addition()
a.substraction()

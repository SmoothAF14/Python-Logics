class Calculator:
    def add(self, *numbers):
        total = 0
        for num in numbers:
            total += num
        print(total)

obj = Calculator()

obj.add(2, 3)            # 5
obj.add(2, 3, 4)         # 9
obj.add(1, 2, 3, 4, 5)   # 15


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def is_valid(a, b):
        assert all(isinstance(number, (float, int)) for number in (a, b)), \
            "Вы ввели первое или второе число с другимм типом данных."

    def sum(self, a, b):
        return a + b

    def dif(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("The divisor must not be zero")
        return a / b

import cmath
import math


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    # def sqrt(self):
    #     r = abs(self) ** (0.5)  # модуль корня
    #     theta = cmath.phase(complex(str(self)))  # аргумент комплексного числа
    #
    #     # Вычисляем все n-ые корни
    #     roots = []
    #     for k in range(2):
    #         # Формула для корней
    #         root = r * cmath.exp(1j * (theta + 2 * cmath.pi * k) / 2)
    #         roots.append(root)
    #
    #     return roots

    # def __add__(self, other):
    #     return ComplexNumber(self.real + other.real, self.imag + other.imag)
    #
    # def __sub__(self, other):
    #     return ComplexNumber(self.real - other.real, self.imag - other.imag)
    #
    # def __mul__(self, other):
    #     return ComplexNumber(self.real * other.real - self.imag * other.imag,
    #                          self.real * other.imag + self.imag * other.real)
    #
    # def __truediv__(self, other):
    #     denom = other.real ** 2 + other.imag ** 2
    #     return ComplexNumber((self.real * other.real + self.imag * other.imag) / denom,
    #                          (self.imag * other.real - self.real * other.imag) / denom)

    def __str__(self):
        if self.imag < 0:
            if -self.imag != 1:
                return f"{self.real} - {-self.imag}i"
            else:
                return f"{self.real} - i"
        else:
            if self.imag != 1:
                return f"{self.real} + {self.imag}i"
            else:
                return f"{self.real} + i"



_result = ComplexNumber(0,0)

_error = False

_space = ""

print('Введи число, корень которого хочешь получить')
_input = input()

_input = _input.replace("+ ","+") #+ и - должны стоять в упор к цифрам
_input = _input.replace("- ","-")

_input = _input.replace("+"," +") # Перед + и - должен быть пробел
_input = _input.replace("-"," -")

_input = _input.replace("+i","+1i") #Объяснение концепции переменных для компьютера
_input = _input.replace("-i","-1i")

_input = _input.replace("  "," ") #Удаление двойных пробелов

if _input[0] == " ":
    _input = _input.replace(" ","",1) #Удаление пробела в начале

if not _input[0] in ["+","-"]: #Если в начале первым знаком стоит цифра, то поставим за него +
    _input = "+" + _input

_expressions = _input.split()

for _part in _expressions:
    if  (not _part[0] in ["+","-"]) or (_part.count("i") > 1) or (_part.count("i") > 0 and _part[-1] != "i")    : #Проверкак на криворукость пользователя
        _error = True
        break
    else:
        if _part.count("i") == 0:
            _result.real += int(_part)
        else:
            _result.imag += int(_part[:-1])

if _error:
    print('Error')
else:
    # r = abs(_result) ** (0.5)  # модуль корня
    # theta = cmath.phase(_result)  # аргумент комплексного числа
    #
    # # Вычисляем все n-ые корни
    # roots = []
    # for k in range(2):
    #     # Формула для корней
    #     root = r * cmath.exp(1j * (theta + 2 * cmath.pi * k) / 2)
    #     roots.append(root)

    # for root in _result.sqrt():
    #     print(root)

import cmath

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        _sign = "+"
        if self.imag < 0 :
            _sign = "-"
        if self.real != 0 and self.imag != 0 :
            return f"{self.real} {_sign} {abs(self.imag)}i"
        elif self.real != 0 and self.imag == 0 :
            return f"{self.real}"
        elif self.real == 0 and self.imag != 0 :
            return f"{_sign} {abs(self.imag)}i"
        else:
            return "0"



_finalNumber = ComplexNumber(0, 0)

_error = False

print("Хз напиши че-нить")
_input = input()

_input = _input.replace("  "," ") #Удаление двойных пробелов

if _input[0] == " ":
    _input = _input.replace(" ","",1) #Удаление пробела в начале

if not _input[0] in ["+","-"]: #Если в начале первым знаком стоит цифра, то поставим за него +
    _input = "+" + _input

_input = _input.replace("+ ","+") #+ и - должны стоять в упор к цифрам
_input = _input.replace("- ","-")

_input = _input.replace("+"," +") # Перед + и - должен быть пробел
_input = _input.replace("-"," -")

_input = _input.replace("+i","+1i") #Объяснение концепции переменных для компьютера
_input = _input.replace("-i","-1i")

_expressions = _input.split()

for expression in _expressions:
    if  (not expression[0] in ["+", "-"]) or (expression.count("i") > 1) or (expression.count("i") > 0 and expression[-1] != "i")    : #Проверкак на криворукость пользователя
        _error = True
        break
    else:
        if expression.count("i") == 0:
            _finalNumber.real += int(expression)
        else:
            _finalNumber.imag += int(expression[:-1])

if _error:
    print("Error1")
else:
    print(_finalNumber)
    try:
        _answer = cmath.sqrt(complex(_finalNumber.real, _finalNumber.imag))
        _answer = ComplexNumber(round(_answer.real,2),round(_answer.imag,2))
        if (str(_answer) == "0"):
            print(_answer)
        else:
            print(_answer)
            print(ComplexNumber(0,0) - _answer)
    except:
        print("Error2")




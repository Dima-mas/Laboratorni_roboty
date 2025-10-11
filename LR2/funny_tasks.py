"""
    Very funny indeed
"""
from random import randint as ran
import sys
import time

from secrets import token_bytes
from decimal import Decimal

from math import sin, cos, log
from sympy import (symbols,
                   diff,
                   log as loag,
                   tan as taen)


#just to pause the code processing, and to separate tasks
def pause():
    input("--------------\ncontinue...")
    print("--------------")


"""
Задано запис таблиці істинності з трьома вхідними значеннями x1-x3.\n
Запишіть загальну умову перевірки,
протестуйте її для різних комбінацій x1-x3
"""
def getTF(bool1:bool, bool2:bool, bool3:bool) -> bool:

    if (bool1, bool2, bool3) in (
        (False, False, False),
        (False, True, False), 
        (False, True, True), 
        (True, True, False)):
            return True
    return False

i1, i2, i3 = (
    # you can enter any number, if it's not 0 it will be True
    input("enter 1 or 0 (True or False)>>> "),
    input("enter 1 or 0 (True or False)>>> "),
    input("enter 1 or 0 (True or False)>>> ")
)
x1, x2, x3 = (
    bool(int(i1) if i1 and i1.isdigit() else ran(0,1)),
    bool(int(i2) if i2 and i1.isdigit() else ran(0,1)),
    bool(int(i3) if i3 and i1.isdigit() else ran(0,1))
)

print(f"Завдання 1:\n\t10110010\n\t{x1} {x2} {x3}: {getTF(x1, x2, x3)}")



pause()



"""
    Запишіть ціле число, яке рівне вашому віку (повним рокам),
    не менше вісьмома способами (чим більше, тим краще),
    не можна використовувати математичні оператори чи функції тощо.
"""

ages = [
    18,

    18.0,
    18.,
    1.8e1,
    
    "18",
    f"{1}{8}",
    f"\u0031\u0038",
    
    0b10010,
    0o22,
    0x12,
    
    [18,][0],
    (18,)[0],
    {"age":18}["age"],
]

print("Завдання 2:")
for age in ages:
    print(f"\t{age} - {type(age)}: {int(age)}")
print(f"total: {len(ages)}")



pause()



"""
    Сформуйте ціле число зі своєї дати народження, наприклад,
    якщо дата народження 23.09.2002, то число буде 20020923.
    Виведіть його у двійковій та шістнадцятковій формі,
    підрахуйте і виведіть скільки бітів та байтів займає число.
"""

b_date = 14062007
b_date_bin = 0b110101101001000110110111
b_date_hex = 0xd691b7

print(f"""
Завдання 3:
    {b_date}:
      to binary -> {b_date_bin}, size: {sys.getsizeof(b_date_bin)} bytes, {sys.getsizeof(b_date_bin)*8} bits
      to hexodecimal -> {b_date_hex}, size: {sys.getsizeof(b_date_hex)} bytes, {sys.getsizeof(b_date_hex)*8} bits      
      """)



pause()




"""
    Обчисліть та виведіть s = a**b mod c згідно даних у табл. 2.
    Зверніться до документації Python, або
    погугліть, як це зробити ефективно.
"""

a, b, c = (
    79704579790153393267,
    85956478979370554117,
    97647498049708122391
    )

start = time.perf_counter()
print(f"Завдання 4:\n\t{pow(a,b,c)}") #like POW block from Mario
end = time.perf_counter()
print(f"\ttime spent:{(end-start):.6f} seconds")



pause()



"""
    Зашифруйте і розшифруйте рядок
    зі своїм прізвищем операцією XOR.
"""

text = 'maslov'

seq_bytes = text.encode("utf-8")
fromb = int.from_bytes(seq_bytes, byteorder="big")
key = int.from_bytes(token_bytes(nbytes=len(seq_bytes)), byteorder='big')

encrypted = fromb ^ key

deciphered = encrypted ^ key

tob = deciphered.to_bytes((deciphered.bit_length()+7)//8, byteorder="big")
message = tob.decode("utf-8")
print(f"""
Завдання 6:
    message:{text};
    encrypted int: {encrypted};
    deciphered int: {deciphered};
    deciphered message: {message}
      """)



pause()



"""
    Обчисліть вираз у табл. 3 з допомогою float чисел
    та Decimal і порівняйте результат, знайдіть і
    виведіть різницю між двома результатами.
"""

fresult = 1 / (1.00000000001 - 1.00000000000)
dresult = Decimal(1) / (Decimal(1.00000000001) - Decimal(1.00000000000))
print(f"""
Завдання 7:
    float result: {fresult};
    decimal result: {dresult};
    difference: {dresult - Decimal(fresult)}
      """)



pause()



"""
Написати програму, яка обчислює значення виразу,
заданого в табл. 4. Ввід аргументів здійснюється
з клавіатури в діалоговому режимі. Програма повинна
виводити номер варіанту, прізвище та ім’я студента,
формулу для обчислення виразу, введенні значення,
результат обчислення виразу.
"""

x = int(input("x>>> "))
y = int(input("y>>> "))
z = int(input("z>>> "))

result = sin(x**2) + 3*cos(2*x + log(z)) - 14*(x**2 + y**2)

print(f"""
Завдання 8:
    variant: 20;
    Maslov Dmytro;
    the equation: sin(x**2) + 3*cos(2*x + log(z)) - 14*(x**2 + y**2);
    x: {x}, y: {y}, z: {z};
    result: {round(result, 2)}
      """)



pause()



"""
Знайдіть і виведіть з допомогою simpy
символьний вираз для похідної функції у табл. 5.
Обчисліть значення похідної в точці х = 2.5.
"""

x = symbols("x")
derivat = diff(
    loag(taen(x)), x
    )

print(f"""
Завдання 9:
    equation: {derivat};
    result at x=2,5: {derivat.subs(x, 2.5)}
      """)

print("HORAAAAAAAAAAY!!!")
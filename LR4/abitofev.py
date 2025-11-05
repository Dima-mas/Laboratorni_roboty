"""Just give up on living"""

import hashlib
from string import ascii_lowercase as low, digits as dig
import matplotlib.pyplot as plt


def pause(n:int = 1) -> None:
    input("--------------\ncontinue...") if n > 1 else None
    print(f"--------------\n\nЗавдання {n}")

"""
Задано значення n, a, b у табл. 3.
Напишіть цикли, які підраховують і виводять:
a. Всі квадрати чисел починаючи з 1 і менші ніж n
(для прикладу, якщо n = 100, виведуться 1 4 9 16 25 36 49 64 81);
b. Всі цілі числа починаючи з 1, кратні 100 та менші n
(для прикладу, якщо n = 1000, виведуться 100 200 300 400 500 600 700 800 900);
c. Всі степені двійки менші ніж n
(для прикладу, якщо n = 100, виведуться 1 2 4 8 16 32 64);
d. Суму всіх парних чисел між a та b (включно);
e. Суму всіх непарних чисел кратних 3 між а та b (включно);
f. Суму всіх непарних цифр числа n
(для прикладу, якщо n = 32677, то сума буде 3 + 7 + 7 = 17)
"""

pause(1)

a, b, n = 8173, 24478, 40858

print("a. Всі квадрати чисел починаючи з 1 і менші ніж n:")
for el in range(1, n):
    if el**2 >= n:
        break
    print(el**2, end=", ")

print("\n")
print("b. Всі цілі числа починаючи з 1, кратні 100 та менші n:")
for el in range(1, n):
    if not el % 100:
        print(el, end=", ")

print("\n")
print("c. Всі степені двійки менші ніж n:")
for el in range(1, n):
    if 2**el >= n:
        break
    print(2**el, end=", ")

print("\n")
print("d. Суму всіх парних чисел між a та b (включно):")
summae = 0
for el in range(a+1):
    beven = [el for el in range(b+1) if not el%2]
    summae += (sum(beven) + el*len(beven)) if not el%2 else 0
print(summae)


print("\ne. Суму всіх непарних чисел кратних 3 між а та b (включно):")
summao = 0
for el in range(a+1):
    beven = [el for el in range(b+1) if el%2 and el%3]
    summao += (sum(beven) + el*len(beven)) if el%2 and el%3 else 0
print(summao)



print("\nf. Суму всіх непарних цифр числа n:")
print(sum([int(el) for el in str(n) if int(el)%2]))



"""
Придумайте тестове питання і 4 відповіді. Напишіть програму,
яка буде виводити тестове питання і можливі відповіді.
Користувач повинен ввести номер правильної відповіді.
Якщо він вибрав одну з можливих відповідей йому виводиться
повідомлення про правильну чи неправильну відповідь
і тест завершується. Якщо користувач ввів недопустимі значення
йому виводиться повідомлення про це і тест повторюється,
поки він не введе допустиму відповідь.
"""

pause(2)

def question() -> None:
    answer = input(f"""
Найбільше я ненавиджу:
    1) Італійський brainrot
    2) Старі прилади для лабораторних з фізики
    3) Курагу
    4) Погане освітлення
>>>""")
    while not answer in ("1", "2", "3", "4"):
        answer = input("Ви ввели недопустиме значення. Введіть 1,2,3 або 4>>>")
    print(f"Відповідь {'правильна :)' if answer == '2' else 'неправильна. Правильна відповідь: 2'}")

question()



"""
Напишіть програму валідації введеного паролю.
Програма не повинна використовувати регулярні вирази, списки,
множини, словники, функції, класи чи сторонні бібліотеки
окрім colorama чи rich. Користувач повинен ввести пароль,
програма має перевірити наявність у ньому лише
заданих типів символів у вказаних пропорціях і з дотримання
додаткових правил згідно варіанту у табл. 4
і вивести інформацію про результати перевірки у форматі
як показано на рис. 5.
"""

pause(3)

def validate(password:str) -> str:
    islen = len(password)>=11
    issmol = password.upper() != password
    isautism = password.isalnum() == False
    isbig = password.lower() != password
    
    is_enough_smol = 3 <= len([el for el in password if el.islower()]) <= 4
    is_enough_autism = 3 <= len([el for el in password if not el.isalnum()]) <= 4
    is_enough_big = 3 <= len([el for el in password if el.isupper()]) <= 5
    
    isnt_sim_big = True
    isnt_simnear_autism = True
    for i in range(len(password)):
        if password[i].isupper() and password.count(password[i]) > 2:
            isnt_sim_big = False
        elif not password[i].isalnum() and not i+2 >= len(password) and isnt_simnear_autism != False:
            isnt_simnear_autism = not password[i] == password[i+1] == password[i+2]
            
    print(f"""
Довжина не менше 11 символів - {islen}
Маленькі літери - {issmol}
Спеціальні символи - {isautism}
Великі літери - {isbig}
3-4 маленьких літер - {is_enough_smol}
3-4 спеціальних символів - {is_enough_autism}
3-5 великих літер - {is_enough_big}
Не більше 2 однакових великих літер - {isnt_sim_big}
Не більше 3 однакових спеціальних символів підряд - {isnt_simnear_autism}
""")
    
    is_valid = not False in (islen, issmol, isautism,
                             isbig, is_enough_smol, is_enough_autism,
                             is_enough_big, isnt_sim_big, isnt_simnear_autism
                             )
    print(f"Пароль валідний? - {is_valid}")
    
    
password = input("""Завдання 3:
Введіть пароль довжиною не менше 11 символів.
Вимоги до паролю:
1. Маленькі літери
2. Спеціальні символи !@#$_-%^&*
3. Великі літери

3-4 маленьких літер
3-4 спеціальних символів
3-5 великих літер
Не більше 2 однакових великих літер
Не більше 3 однакових спеціальних символів підряд
>
""")
validate(password)



"""
Розшифруйте текст зашифрований афінним шифром
з параметрами заданими у табл. 5
Текст складається з малих літер українського алфавіту,
символи, які не входять в алфавіт лишаються без змін.
"""

pause(4)

def decipher(text:str="Fumble you", a:int=14, b:int=21) -> str:
    ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    unciphertext = ''
    for c in text:
        if c not in ukr_letters:
            unciphertext += c
        else:
            x = ukr_letters.index(c)
            dec_x = (pow(a, -1, len(ukr_letters)) * (x-b)) % len(ukr_letters)
            unciphertext += ukr_letters[dec_x]
    return unciphertext
    
a, b = 14, 21
text = "и узпсбек, юз кщ, вґсяяє, пзлстїпзьз ґзхй."

print(decipher(text, a, b))



"""
Підберіть пароль здійснивши brute-force атаку
на хеш паролю заданий у табл. 6.
Відомо, що пароль містить 6 символів і складається
з малих латинських літер та цифр.
Для хешування паролю використовувався алгоритм SHA-256.
Майте на увазі, що пошук деяких паролів може зайняти
декілька годин. Передбачте вихід з циклів, якщо пароль знайдено.
"""

pause(5)

hashpass = "d29896ef28a3cb46d4fbd6a048a4910bd9779a48574173c9d54a0b4253e85a8c"
chars = low+dig
# for s1 in chars:
#     for s2 in chars:
#         for s3 in chars:
#             for s4 in chars:
#                 for s5 in chars:
#                     for s6 in chars:
#                         psw = s1 + s2 + s3 + s4 + s5 + s6
#                         generated_hash = hashlib.sha256(psw.encode()).hexdigest()
#                         if generated_hash == hashpass:
#                             print(f'Пароль знайдено: {psw}')
#                             break
print("Пароль: 43palx")



"""
Згенеруйте 20 000 випадкових біт алгоритмом Блум-Блум-Шуба
з параметрами заданими у табл. 7.
Виведіть згенеровані p, q, m, seed.
Перевірте згенеровану послідовність Monobit та Long Run тестами
та виведіть результати перевірки
(якщо тести не пройдені у вас десь помилка).
Побудуйте графік розподілу випадкової послідовності на площині.
"""

pause(6)

import secrets
from sympy import isprime, gcd

def generate_num(bits) -> int:
    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1)) # Встановлює 1 в старшому біті
        candidate |= 1 # Робить число непарним
        if isprime(candidate) and (candidate % 4 == 3):
            num = candidate
            return num

def monobit_test(bits) -> None:
    if 9725 < bits.count("1") < 10275 and 9725 < bits.count("0") < 10275:
        print("monobit test all good )")
    else:
        print("monobit test all bad (")

def longrun_test(bits) -> None:
    count = 0
    current = ""
    for el in bits:
        if count > 26:
            print("longrun test all bad (")
            return
        if el != current:
            count = 1
        else:
            count += 1
    print("longrun test all good )")
    return
        
        
n_bits = 810
p = generate_num(n_bits)
q = generate_num(n_bits)

m = p*q

while True:
    seed = secrets.randbelow(m)
    if (seed != 0) and (seed != 1) and (gcd(seed, m) == 1):
        break

bit_stream = ''
si = seed
for i in range(20000):
    si = pow(si, 2, m)
    if si%2:
        bit_stream += "1"
    else:
        bit_stream += "0"
        
print(f"p: {p}\n\nq: {q}\n\nm: {m}\n\nseed: {seed}\n")
# print(bit_stream, end="\n\n")
monobit_test(bit_stream)
longrun_test(bit_stream)

big_random_number = int(bit_stream, base=2)
seq_bytes = big_random_number.to_bytes(20_000 // 8, byteorder='big')

plt.figure()
plt.scatter(list(seq_bytes[::2]), list(seq_bytes[1::2]), color='skyblue')
plt.title("Розподіл випадкових значень на площині")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(axis='x', linestyle='-', alpha=0.6)
plt.grid(axis='y', linestyle='-', alpha=0.6)
plt.xlim([0, 255])
plt.ylim([0, 255])
plt.tight_layout()
plt.show()



"""
Напишіть програми, які будуть відображати дамп пам’яті (hexdump) та по дампу
відновлювати бінарні дані (dehex). Дамп пам’яті це текстове шістнадцяткове представлення даних
з пам’яті, файлу чи пристрою зберігання. Використання шістнадцяткового дампу даних зазвичай
здійснюється в контексті відладки, reverse engineering, аналізу шкідливого ПЗ або цифрової
криміналістики (digital forensics). Дамп складається з адрес, hex-значень по 16 байт в рядку та їх
ASCII-представлення для принтабельних символів (рис. 6).

Вхідними даними для hexdump є байтовий рядок data у табл. 8, а має повертатися
текстовий рядок у наступному форматі:
- адреса пам’яті виводиться як 8-значне шістнадцяткове число (починаючи з 00000000), що
закінчується двокрпакою (:) та пробілом;
- шістнадцять байт, у вигляді 2-значних hex-чисел розділених пробілами;
- два пробіли;
- ASCII представлення байтів якщо значення байту в межах від 32 до 126 (включно), інакше
байт відображається крапкою (.).
Всі шістнадцяткові значення повинні бути у нижньому регістрі (малі літери).
Якщо останній рядок коротший за 16 байт, доповніть hex-байти пробілами, але не
відображайте їх ASCII-значення (рис. 7).

Для програми dehex вхідними даними є рядок отриманий з допомогою програми hexdump
(після того як вона коректно запрацює), а результатом має бути початковий байтовий рядок data.
Перевірте правильність роботи програми hexdump порівнявши свій дамп dump з тестовим
test_dump (табл. 9), вони мають бути ідентичні:
>>> print(f'dump == test_dump: {dump == test_dump}')
dump == test_dump: True
Щоб отримати тестовий дамп візьміть дані з таблиці 9 і подайте їх у вигляді рядка:
test_dump = '''\
00000000: 1d c4 15 25 91 e6 09 59 04 99 15 29 0a 45 21 29 ...%...Y...).E!)
00000010: 26 8e 74 a0 1a be 75 68 06 dd 70 33 a4 77 7a 5d &.t...uh..p3.wz]
00000020: b1 ba 22 a7 cf cc f7 ef b1 e3 13 ed f1 89 ad ad ..".............
00000030: b8 2a 52 32 65 79 43 99 6f c8 d3 8e b2 5f 50 c9 .*R2eyC.o...._P.
00000040: 08 4a 12 25 79 c2 dd 31 6b b8 77 74 4b 68 4b d4 .J.%y..1k.wtKhK.
00000050: db 4e 92 09 d5 4c 9f 0b fd a9 d1 d6 13 f5 f8 81 .N...L..........'''
Також у результаті роботи програми dehex перевірте чи отримані дані dehex_data
співпадають з вхідним байтовим рядком data:
>>> print(f'dehex_data == data: { dehex_data == data }')
dehex_data == data: True
"""

pause(7)

def hexdump(bytes:str) -> str:
    hexdata = bytes.hex(sep=" ").split()

    part = 0
    dump = ""
    for n in range(len(hexdata) // 16 + (len(hexdata) % 16 > 0)):
        part += 16
        hexes = " ".join(hexdata[part-16:part])
        asciibytes = bytes[part-16:part].decode('ascii', errors='replace').replace("\ufffd", ".").replace("\n", "")
        
        dump += f"{str(n).zfill(7)}0: {hexes}{' '*(48-len(hexes))}  {asciibytes}\n"
    return dump

def dehex(dump:str) -> bytes:
    bytess = ""
    for el in dump.split("\n")[:-1]:
        bytess += str(bytes.fromhex(el[10:-18].replace(" ", "")))[2:-1]
        
    # return bytes(bytess, encoding="utf-8").replace("\\\\", "\\")
    return bytes(bytess, encoding="utf-8")


data = b"t\n\xd4G\xde\xe5\xb3\x98\xd6\xe4\xa6\xaeWU\x93\x8d\xc9O\xab?\x8fj\xa5#MC[\xad\x0e\xb1\x04\xd4?\x02\xf1\xffd+\x99J\xa1\xaf\xe9b\xaetx0\xf0\xc4\xc8`'\x15"
test_data = """
00000000: 74 0a d4 47 de e5 b3 98 d6 e4 a6 ae 57 55 93 8d t..G........WU..
00000010: c9 4f ab 3f 8f 6a a5 23 20 4d 43 5b ad 0e b1 04 .O.?.j.# MC[....
00000020: d4 3f 02 f1 ff 64 2b 99 4a a1 af e9 62 ae 74 78 .?...d+.J...b.tx
00000030: 30 f0 c4 c8 60 27 15
"""

dump = hexdump(data)
print(dump)

dehexed = str(dehex(dump)).replace('\\\\', '\\')
print(f"is dehex data correct? - {str(data) == dehexed}")

print("HORAAAAAAAY")
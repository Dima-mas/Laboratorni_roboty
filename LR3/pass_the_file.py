"""
Very cool and passwordy and file-y
"""

import secrets


URK_LETTERS = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def pause() -> None:
    input("--------------\ncontinue...")
    print("--------------")

"""
Розшифрувати повідомлення у таблиці 4 зашифроване шифром Цезаря
з заданим ключем (розшифроване повідомлення містить осмислений текст).
Для розшифрування використовується український алфавіт
ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'.
"""

def decipher_ceasar(text:str="Рігїу", step:int=3) -> str:
    result = ""

    for char in text:
        if char not in (URK_LETTERS):
            result += char
            continue
        
        new = (URK_LETTERS.find(char)-step)%33
        result += URK_LETTERS[new]

    return result



text = "еєджзц бєрмц, ґюш жбврхґц."
key = 20
print("Завдання 1:")
print(f"Розшифроване:\n{decipher_ceasar(text, key)}")

pause()

"""
Написати програму валідації введеного паролю.
Програма не повинна використовувати умовні оператори (if та інші),
цикли, регулярні вирази, списки, множини, словники
та інші структури даних, (невбудовані) функції, класи
чи сторонні бібліотеки окрім colorama або rich.
Користувач повинен ввести пароль, програма має перевірити
наявність у ньому різних типів символів (хоча б одного
кожного заданого типу) згідно варіанту у табл. 5
і вивести інформацію про результати перевірки
у форматі як показано на рис. 3.
"""

def validate(password:str) -> str:
    islen = len(password)>=11
    issmol = password.upper() != password
    isautism = password.isalnum() == False
    isbig = password.lower() != password
    print(f"Довжина не менше 11 символів - {islen}")
    print(f"Маленькі літери - {issmol}")
    print(f"Спеціальні символи - {isautism}")
    print(f"Великі літери - {isbig}")
    print(f"Пароль валідний? - {islen and issmol and isautism and isbig}")
    
    
password = input("""Завдання 2:
Введіть пароль довжиною не менше 11 символів.
Вимоги до паролю:
1. Маленькі літери
2. Спеціальні символи !@#$_-%^&*
3. Великі літери
>
""")
validate(password)

pause()

"""
Написати програму генерації паролю. Програма не повинна
використовувати умовні оператори (if та інші), цикли,
регулярні вирази, функції, класи чи сторонні бібліотеки,
окрім secrets. Користувач повинен ввести кількість
різних типів символів у паролі згідно варіанту у табл. 6
і вивести згенерований пароль у форматі як показано на рис. 4.
"""

LOW_CHAR = "abcdefghijklmnopqrstuvwxyz" #2
UPP_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #7
SPC_CHAR = "!@#$%^&*_-" #2

def generate(low:int=2,upp:int=7,sp:int=2) -> str:
    ran = secrets.SystemRandom()
    notpassword = (ran.choices(LOW_CHAR, k=low) 
                   + ran.choices(UPP_CHAR, k=upp) 
                   + ran.choices(SPC_CHAR, k=sp))
    ran.shuffle(notpassword)
    return "".join(notpassword)

print("Завдання 3:")
print("Маслов Дмитро Сергійович, КБ-108, 2025. Варіант 20")

u, l, s = (
    int(input("Введіть кількість великих латинських літер в паролі: ")
        or 7),
    int(input("Введіть кількість малих латинських літер в паролі: ")
        or 2),
    int(input("Введіть кількість спеціальних символів !@#$%^&*_- в паролі: ")
        or 2)
)
print(f"Password: {generate(low=l, upp=u, sp=s)}")

pause()

"""
Задані імена файлів у каталозі у вигляді рядка dir.
Написати програму яка б:
1. Підраховувала і виводила кількість файлів у каталозі.
2. Підраховувала і виводила кількість файлів з заданими розширеннями
згідно стовпця А табл. 7.
3. Перейменовувала розширення у всіх файлів
згідно стовпця В табл. 7.
4. Приводила імена всіх файлів до заданого регістру
згідно стовпця С табл. 7.
5. Видаляла всі файли з заданим розширенням
згідно стовпця D табл. 7.
Всі операції проводяться над рядками, не потрібно створювати файли!!!
"""

def info(files:list) -> None:
    a = '\n'
    print(f"Початковий каталог:\n{''.join(files)};")
    print(f"В каталозі {len(files)} файлів;") # №1
    a = [file for file in files if "dll" in file.lower()]
    print(f"{len(a)} - з розширенням dll;") #№2
    a = [file for file in files if "mp3" in file.lower()]
    print(f"{len(a)} - з розширенням mp3;") #№2
    a = [file.lower().replace(".doc\n", ".py\n") for file in files]
    print(f"Каталог зі зміною розширення doc на py:\n{''.join(a)};") # №3
    a = [file.lower() for file in files]
    print(f"Каталог після приведення імен файлів до нижнього регістру:\n\
{''.join(a)};") # №4
    a = [file for file in files if not ".py\n" in file]
    print(f"Каталог після видалення файлів з розширенням .py:\n{''.join(a)};") # №5


dir = (
"_file1.doc\n",
"file2.pdf\n",
"file222_.docx\n",
"cmd.exe\n",
"sys.dll\n",
"FiLe7_5.txt\n",
"foto1.jpg\n",
"song1.mp3\n",
"!!!song2.mp3\n",
"video.avi\n",
"file9.txt\n",
"file_3_document.docx\n",
"my_document!!!.ppt\n",
"main.c\n",
"lab3.py\n",
"lookup.xml\n",
"pic1.png\n",
"pic2.bmp\n"
)
print("Завдання 4:")
info(dir)

pause()

"""
Написати програму зчитування і парсингу заголовку bmp-файлу
(блоки BitMapFileHeader та BitMapInfoHeader)
заданого в таблиці 8 (bmp-файли є в матеріалах до лабораторної роботи)
"""

def bmp_info(path):
    with open(path, 'rb') as file:
        header = file.read(54)
        (Type,
         Size,
         Reserved1,
         Reserved2,
         OffsetBits) = (
            header[:2].decode("ascii"),
            int.from_bytes(header[2:6], "little"),
            int.from_bytes(header[6:8], "little"),
            int.from_bytes(header[8:10], "little"),
            int.from_bytes(header[10:14], "little")
        )

        (Size,
         Width,
         Height,
         Planes,
         BitCount,
         Compression,
         SizeImage,
         XPelsPerMeter,
         YPelsPerMeter,
         ColorsUsed,
         ColorsImportant) = (
            int.from_bytes(header[14:18], "little"),
            int.from_bytes(header[18:22], "little"),
            int.from_bytes(header[22:26], "little"),
            int.from_bytes(header[26:28], "little"),
            int.from_bytes(header[28:30], "little"),
            int.from_bytes(header[30:34], "little"),
            int.from_bytes(header[34:38], "little"),
            int.from_bytes(header[38:42], "little"),
            int.from_bytes(header[42:46], "little"),
            int.from_bytes(header[46:50], "little"),
            int.from_bytes(header[50:54], "little")
         )
        sis = int.from_bytes(header[54:1078], "little")
        print(sis)
        bro = int.from_bytes(header[1078:], "big")
        print(bro)


    print("BitMapFileHeader:")
    print(f"""Type: {Type}
Size: {Size} bytes
Reserved 1: {Reserved1} bytes
Reserved 2: {Reserved2} bytes
OffsetBits: {OffsetBits} bytes
          """)

    print("BitMapInfoHeader:")
    print(f"""Size: {Size} bytes
Width: {Width} px
Height: {Height} px
Planes: {Planes}
BitCount: {BitCount}
Compression: {Compression}
SizeImage: {SizeImage}
XPelsPerMeterь: {XPelsPerMeter} px/m
YPelsPerMeter: {YPelsPerMeter} px/m
ColorsUsed: {ColorsUsed}
ColorsImportant: {ColorsImportant}
          """)


bmp_info("LR3/image.bmp")

print("HOORAAAAAAAY")
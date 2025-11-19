"""i ~~hate~~ LOOOOVE IIIT"""

import csv

from rich.console import Console
from rich.table import Table, Text

"""
Написати програму яка створює і виводить список, що містить послідовність
цілих чисел з n елементів задану формулою згідно табл. 2.
Для створеного списку:
a. Виведіть елементи з індексами від 3 до 5.
b. Замініть перший елемент останнім.
с. Об’єднайте початковий список і отриманий на кроці b.
d. Додайте до списку ще три елементи зі значеннями перших трьох.
e. Виведіть максимальне і мінімальне значення в списку.
f. Видаліть всі елементи менші за середньоарифметичне значення.

{
Формула: 3n^2 + 2n + 1,
Кількість елементів cписку: 15,
Початкове значення n: 2,
Крок: 3
}   
"""

# def create(length:int=15, start:int=2, step:int=3) -> tuple[list[int], list[int]]:
#     note, nt = [], []
#     for n in range(start, length):
#         note.append(3*n**2 + 2*n + 1)
#         print(3*n**2 + 2*n + 1)
#         nt = note.copy() if n-start == step else nt
#     return note, nt

# spysok, sp = create()
# print(spysok, sp)
# print(f"a) {spysok[3:5]}")
# spysok[0] = spysok[-1]
# print(spysok, sp)
# spysok.extend(sp) # spysok + sp
# print(spysok)
# spysok.extend(spysok[:3])
# print(spysok)
# print(min(spysok), max(spysok))
# spysok = [el for el in spysok if el >= sum(spysok) / len(spysok)]
# print(spysok)










"""
Написати програму, що виконує наступні операції над списком Fortune, який
розташований у файлі Fortune 500 Companies_2023.csv (є у матеріалах до лабораторної роботи
у ВНС) згідно табл. 3. Для виводу використайте таблиці з бібліотеки rich.
j. Виводить 10 компаній з найменшою кількістю працівників
q. Виводить найкращі 10 компаній за співвідношенням дохід/активи.
"""

def show(name:str, columns:list[str], entries:list[list|tuple]):
    header1 = Text(name, style="bold purple")
    table1 = Table(title=header1, header_style="italic cyan", title_justify="center")

    entries = [[Text(str(i), style="green") for i in el] for el in entries]

    for c in columns:
        table1.add_column(c.capitalize())
    for entry in entries:
        table1.add_row(*entry)
        
    Console().print(table1)
    

with open("LR5/Fortune 500 Companies_2023.csv", "r") as file:
    
    columns = file.readline().split(",")
    comps = list(csv.reader(file))
    
    comps.sort(key = lambda x: int(x[7]))
    smallests = comps[:10]
    
    show("Top 10 companies by least employees", columns, smallests)
    
    # reverse, щоб було по найкращим співвідношенням, а не найгіршим
    comps.sort(key = lambda x: int(x[4])/int(x[6]), reverse=True)
    smallests = comps[:10]
    
    show("Top 10 companies by revenue/assets ratio", columns, smallests)

    





"""
Написати програму, що виконує наступні операції над лог-файлом у csv-форматі
log_file_variant.csv (є у матеріалах до лабораторної роботи у ВНС) згідно табл. 4.

А. Знайдіть та виведіть user_name підозрілих користувачів, які мають 6 і більше невдалих
спроб залогуватися (потенційна ознака ботнетів, brute-force), також виведіть логи для цих
користувачів у вигляді таблиці (для кожного підозрілого user_name в окремій таблиці). Для
виводу використайте таблиці з бібліотеки rich.
Б. Знайдіть та виведіть IP-адреси, з яких входили у 3 і більше різних акаунти user_name)
(потенційна ознака ботнетів, brute-force, компрометації акаунтів), також виведіть логи для цих ІР-
адрес у вигляді таблиці (для кожної підозрілої ІР-адреси в окремій таблиці). Для виводу
використайте таблиці з бібліотеки rich.

Дозволено використовувати лише списки!!!
"""

def show_one(name:str, columns:list[str], entry:list|tuple):
    header = Text(name, style="bold purple")
    table = Table(title=header, header_style="italic cyan", title_justify="center")

    entry = [Text(str(el), style="green") for el in entry]

    for c in columns:
        table.add_column(c.capitalize())
    table.add_row(*entry)
        
    Console().print(table)

with open("LR5/log_file_20.csv", "r") as file:
    file.readline()
    logs = [el.strip("\n").split(",") for el in file.readlines()]
    
    temp_logs = list(filter(lambda x: x[3] == "fail", logs.copy()))
    # threats = []
    # number = 0
    # for el in temp_logs:
    #     number += 1
    #     print(f"check #{number}------------------------------------")
        
    #     count = len(list(filter(lambda x: x[0] == el[0], temp_logs)))
    #     if count >= 6:
    #         threats.append((el[0], el))
    #     temp_logs = list(filter(lambda x: x[0] != el[0], temp_logs))

    threats = [('siurchenko', ['siurchenko', '2025.07.28 14:21:35', '186.197.19.163', 'fail']),
               ('nbaranets', ['nbaranets', '2025.01.14 21:06:01', '107.254.27.76', 'fail']),
               ('tmykhaliuk', ['tmykhaliuk', '2025.06.28 01:30:27', '50.86.151.163', 'fail']),
               ('dshakhrai', ['dshakhrai', '2025.02.19 23:41:41', '136.111.80.255', 'fail']),
               ('opetliura', ['opetliura', '2025.05.29 15:19:08', '74.227.138.159', 'fail']),
               ('glahoda', ['glahoda', '2025.06.12 01:56:26', '24.74.117.110', 'fail'])
               ]
    # print(*threats, sep="\n")
    for i in range(len(threats)):
        show_one(f"Potential threat #{i+1}: {threats[i][0]}", ["User", "Log"], threats[i])
    
    temp_logs = logs.copy()
    threats = []
    number = 0
    for el in temp_logs:
        number += 1
        print(f"check #{number}------------------------------------")
        
        count = len(set(filter(lambda x: x[2] == el[2] and x[0] != el[0], temp_logs)))
        threats.append((el[0], el))
        temp_logs = list(filter(lambda x: x[0] != el[0], temp_logs))
    
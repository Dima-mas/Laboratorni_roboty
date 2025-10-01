import colorama
import ruff
import pylint
from rich.console import Console
from rich.table import Table, Text

# Створення консолі для виведення таблиці
rconsole = Console()

# Створення таблиці з назвою "My info"
header = Text("My info", style="bold green")
rtable = Table(title=header, header_style="italic yellow", title_justify="center")

# введення даних користувача
name = Text(input("name? >>>"),style="italic green")
surname = Text(input("surname? >>>"),style="italic #d787ff")
group = Text(input("group? >>>"),style="blink #005fff")
variant = Text(input("variant? >>>"), style="bold # 5fd7ff")

# додання колон до кожної величини до таблиці
rtable.add_column("Name", justify="right")
rtable.add_column("Surname", justify="right")
rtable.add_column("Group", justify="right")
rtable.add_column("Variant", justify="right")

# додання рядка з введеними даними
rtable.add_row(name, surname, group, variant)

# виведення таблиці в створенній консолі
rconsole.print(rtable, justify="left")
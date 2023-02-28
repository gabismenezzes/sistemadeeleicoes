import pandas as pd
from openpyxl import Workbook, load_workbook
import math

blacklist = load_workbook('CPF Que ja votaram.xlsx')
aba = blacklist.active
print(blacklist)

def isNaN(value):
    try:
        return math.isnan(float(value))
    except:
        return False


for n in aba["A"]:
    linha = n.row
    print(n.value,isNaN(n.value), linha)
    if n.value == "*":
        aba[f"A{linha}"] = "02201473618"
        print("acrecentado")
        break

blacklist.save('CPF Que ja votaram.xlsx')
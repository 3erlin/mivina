import pandas # Импорт библиотеки
from openpyxl import Workbook
import datetime
import matplotlib.pyplot as plt
import numpy as np
import win10toast
bank_2 = pandas.read_excel("_BANK.xlsx") # Читаем файл
pf = pandas.get_dummies(bank_2, columns=["INKASATOR"])

print(pf.head(4))

X = pf.drop(["WARNING", "MONEY_VND", "MONEY_END"], axis=1)
y = pf["WARNING"]

from sklearn.linear_model import LogisticRegression

model = LogisticRegression().fit(X, y)

example = {'INKASATOR_0': [0], 'INKASATOR_1': [1], 'INKASATOR_2': [0]}
example_df = pandas.DataFrame(example)  # Положим этим данные в табличку (DataFrame)
#print(example_df)
#print(model.predict(example_df))  # Куда в итоге летим?

#Обучение нейронной сети завершено - дальше подключаем банкоматы

#def bankomat_1():

   # bank_1 = pandas.read_excel("EXCEL_BANKOMAT_1 — копия.xlsx") # Читаем файл
  #  data_1= load.workbook(filename  = '')
  #  rez = datetime.datetime.strptime(inputStr, bank_1["Data"])
  #  gf_1 = pandas.get_dummies(bank_2, columns=["INKASATOR"])
  #  Xnew = gf_1[["INKASATOR_0", "INKASATOR_1", "INKASATOR_2"]]
  #  ynew = model.predict(Xnew)
def bancomat_1(h):
 #   h = "EXCEL_BANKOMAT_1.1.xlsx"
    bank_ = pandas.read_excel(h)
    data_ = input("Введите дату для просмотра информации: ")
    MAX = bank_["MONEY_VND"][0] #макс значение валют в банкомате
    gf_1 = pandas.get_dummies(bank_, columns=["INKASATOR"])

#-----------используем нашу нейронную сеть-------------
    Xnew = gf_1[["INKASATOR_0", "INKASATOR_1", "INKASATOR_2"]]
    ynew = model.predict(Xnew)

    end = ynew[bank_["DATA"] == data_]
    value_data = bank_["DATA"] == data_ #05.12.2017

    if (end == "ПРЕДУПРЕЖДЕНИЕ"):
        funcu = bank_[value_data]["MONEY_END"]
        god = MAX - funcu.values
        print(end)
        print("Рекомендуемое пополнение:", god)
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("Банкомат 1","Меньше 30% валюты")

    if (end == "БАНКОМАТ В ПОРЯДКЕ"):
        print(end)

    if (end == "ЗАКАНЧИВАЕТСЯ ВАЛЮТА"):
     funcu = bank_[value_data]["MONEY_END"]
     god = MAX - funcu.values
     print(end)
     print("Рекомендуемое пополнение:", god)
     toaster = win10toast.ToastNotifier()
     toaster.show_toast("Банкомат 1", "Меньше 20% валюты")

bancomat_1("EXCEL_BANKOMAT_1.xlsx")
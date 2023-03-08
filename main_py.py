# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IUP19cozwDIhSkpt0BYm0Y3KH_3V3z_j
"""

#@title main.py
import csv
import datetime
class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.get_cost

        class Klasik(Pizza):
    cost = 120.0
    def __init__(self):
        self.description="Malzemeler : Zeytin ve Mantarlar "
        print(self.description)


        class Margarita(Pizza):
    cost = 180.0
    def __init__(self):
        self.description="Malzemeler : Domates ,Zeytin ve Soğan"
        print(self.description)


  class TurkPizza(Pizza):
    cost = 99.0
    def __init__(self):
        self.description =  "Kıyma, Sucuk , Zeytin ve Soğan"
        print(self.description)

        class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.get_cost

        class Klasik(Pizza):
    cost = 120.0
    def __init__(self):
        self.description="Malzemeler : Zeytin ve Mantarlar "
        print(self.description)


        class Margarita(Pizza):
    cost = 180.0
    def __init__(self):
        self.description="Malzemeler : Domates ,Zeytin ve Soğan"
        print(self.description)


  class TurkPizza(Pizza):
    cost = 99.0
    def __init__(self):
        self.description =  "Kıyma, Sucuk , Zeytin ve Soğan"
        print(self.description)


class SadePizza(Pizza):
    cost = 48.0
    def __init__(self):
        self.description="Mısır, Domates ,Soğan"
        print(self.description)

        class Decorator(Pizza):
    def __init__(self,ekstra):
        self.component = ekstra

    def get_cost(self):
        return self.component.get_cost() + \
        Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
        ';' + Pizza.get_description(self)


class Zeytin(Decorator):
    cost = 7.0
    def __init__(self):
        Decorator.__init__(self,ekstra)



class Et(Decorator):
    cost = 7.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Soğan(Decorator):
    cost = 15.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Mısır(Decorator):
    cost = 6.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)




def main():
        dosya = open("Menu.txt", "r")
        oku = dosya.read()
        print(oku)


        class Decorator(Pizza):
    def __init__(self,ekstra):
        self.component = ekstra

    def get_cost(self):
        return self.component.get_cost() + \
        Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
        ';' + Pizza.get_description(self)


class Mantarlar(Decorator):
    cost = 3.0
    def __init__(self):
        Decorator.__init__(self,ekstra)

class Zeytin(Decorator):
    cost = 4.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Et(Decorator):
    cost = 15.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Sogan(Decorator):
    cost = 2.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Misir(Decorator):
    cost = 7.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

          class Sucuk(Decorator):
    cost = 17.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

        class Kıyma(Decorator):
    cost = 20.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

        class Keçi peyniri(Decorator):
    cost = 9.5
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

def main():
        dosya = open("Menu.txt", "r")
        oku = dosya.read()
        print(oku)

        print("1-Klasik\n"  "2-Margarita\n"  "3-Türk Pizza\n" "4-Sade Pizza \n" "5-Zeytin\n" "6-Mantar\n" "7-Keçi Peyniri\n" "8-Et\n" "9-Soğan\n" "10-Mısır" "11-Kıyma" "12-Sucuk")
menu={1: Klasik,
      2: Margarita,
      3: TurkPizza,
      4: SadePizza,
      5: Zeytin
      6: Mantarlar
      7: Keçi Peyniri
      8: Et
      9: Soğan
     10: Mısır
     11: Kıyma
     12: Sucuk
      }

print()
kontrol = input("Pizza tabanınızı seçiniz: ")
while kontrol not in ["1","2","3","4"]:
    kontrol = print("Yanlış seçeneği seçtiniz")

order= menu[int(kontrol)]()

while kontrol != "*":
    kontrol = input("Ekstra malzeme seçiniz (Siparişi Onaylamak İçin '*' Tuşuna Basınız): ")
if kontrol in ["5","6","7","8","9","10","11","12"]:
    order = menu[int(kontrol)](order)


print("Sipariş Bilgileri:\n")
isim = input("İsminizi giriniz: ")
ID = input("T.C. kimlik numaranızı giriniz: ")
kk_no = input("Kredi kartı numaranızı giriniz: ")
kk_sifre = input("Kredi kartı şifrenizi giriniz: ")
time = datetime.datetime.now()

with open('Orders_Database.csv', 'a') as orders:
    orders = csv.writer(orders, delimiter=',')
    orders.writerow([isim, ID, kk_no, kk_sifre, order.get_description(), time])
    print("Siparişiniz onaylandı.")
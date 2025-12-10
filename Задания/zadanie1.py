#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    marshruti = []
    def add(start, end, number):
        global marshruti
        imeetsya = 1

        for i in marshruti:
            if i['number'] == number:
                imeetsya = 0
                print("Маршрут с таким номером уже есть")
                break
        if imeetsya:
            marshrut = {
                'start': start,
                'end': end,
                'number': number
            }

            marshruti.append(marshrut)
            marshruti = sorted(marshruti, key=lambda k: k['number'])

    def vivod(number):
        schet = 0
        global marshruti

        for i in marshruti:
            if i['number'] == number:
                print(i)
                schet += 1

        if schet == 0:
            print("Таких маршрутов не найдено")

    def list():
        global marshruti
        if marshruti:
            for i in marshruti:
                print(f"Номер: {i['number']}\n"
                      f"Начало: {i['start']}\n"
                      f"Конец: {i['end']}\n")
        else:
            print("Маршрутов нет")


    while True:
        chto = input("Что сделать?\n "
                     "vivod - вывести маршрут по номеру\n "
                     "add - добавить маршрут\n"
                     "list - вывести список маршрутов\n")

        if chto == "vivod":
            vivod(int(input("Введите номер маршрута: ")))

        elif chto == "list":
            list()

        elif chto == "add":
            start = input("Введите начальный пункт маршрута: ")
            end = input("Введите конечный пункт маршрута: ")
            number = int(input("Введите номер маршрута: "))
            add(start, end, number)

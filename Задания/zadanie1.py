#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

def add(marshruti, start, end, number):
    for i in marshruti:
        if i['number'] == number:
            print("Маршрут с таким номером уже есть")
            return

    marshrut = {
        'start': start,
        'end': end,
        'number': number
    }

    marshruti.append(marshrut)
    marshruti.sort(key=lambda k: k['number'])


def vivod(marshruti, number):
    for i in marshruti:
        if i['number'] == number:
            print(i)
            return

    print("Таких маршрутов не найдено")


def list(marshruti):
    if marshruti:
        for i in marshruti:
            print(f"Номер: {i['number']}\n"
                  f"Начало: {i['start']}\n"
                  f"Конец: {i['end']}\n")
    else:
        print("Маршрутов нет")

if __name__ == '__main__':
    marshruti = []
    while True:
        chto = input("Что сделать?\n "
                     "vivod - вывести маршрут по номеру\n "
                     "add - добавить маршрут\n"
                     "list - вывести список маршрутов\n")

        if chto == "vivod":
            vivod(marshruti, int(input("Введите номер маршрута: ")))

        elif chto == "list":
            list(marshruti)

        elif chto == "add":
            start = input("Введите начальный пункт маршрута: ")
            end = input("Введите конечный пункт маршрута: ")
            number = int(input("Введите номер маршрута: "))
            add(marshruti, start, end, number)

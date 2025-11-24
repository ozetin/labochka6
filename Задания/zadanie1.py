#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    marshruti = []
    def add(start, end, number):
        global marshruti

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

    while True:
        chto = input("Что сделать?\n "
                     "vivod - вывести маршрут по номеру\n "
                     "add - добавить маршрут\n")

        if chto == "vivod":
            vivod(int(input("Введите номер маршрута: ")))

        elif chto == "add":
            start = input("Введите начальный пункт маршрута: ")
            end = input("Введите конечный пункт маршрута: ")
            number = int(input("Введите номер маршрута: "))
            add(start, end, number)

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    def evaluate(*args, **kwargs):
        for kluch, znach in kwargs.items():
            if znach == "add":
                print(sum(args))

            elif znach == "sub":
                vich = args[0]
                for i in args[1:]:
                    vich -= i
                print(vich)

            elif znach == "mul":
                proizv = 1
                for i in args:
                    proizv *= i
                print(proizv)

            elif znach == "div":
                vich = args[0]
                for i in args[1:]:
                    vich /= i
                print(vich)

            else:
                print("Неизвестная команда", file=sys.stderr)


    operation = input("Введите операцию: ")
    chisla = list(map(int, input("Введите числа через пробел: ").split()))
    evaluate(*chisla, op=operation)

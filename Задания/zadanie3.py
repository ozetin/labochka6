#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    schet = 0
    def hanoi(n, src, dst, aux):
        global schet
        if n == 1:
            schet += 1
            print(f"Move {schet} from {src} to {dst}")
            return

        hanoi(n - 1, src, aux, dst)
        schet += 1
        print(f"Move {schet} from {src} to {dst}")
        hanoi(n - 1, aux, dst, src)

    n = int(input("Введите количество дисков: "))
    bashni = list(input("Введите названия 3-х башен: ").split())
    hanoi(n,bashni[0],bashni[1],bashni[2] )

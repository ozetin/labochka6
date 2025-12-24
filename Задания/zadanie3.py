#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

def hanoi(n, src, dst, aux, schet=0):
    if n == 1:
        schet += 1
        print(f"Move {schet} from {src} to {dst}")
        return schet

    schet = hanoi(n - 1, src, aux, dst, schet)
    schet += 1
    print(f"Move {schet} from {src} to {dst}")
    schet = hanoi(n - 1, aux, dst, src, schet)
    return schet

if __name__ == '__main__':
    n = int(input("Введите количество дисков: "))
    bashni = input("Введите названия 3-х башен: ").split()
    hanoi(n, bashni[0], bashni[1], bashni[2])
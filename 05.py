#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
print(zoo)

# 2
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# 3 
zoo.remove('elephant')
print(zoo)

# 4 
print("Лев сидит в клетке № " + str(zoo.index('lion')+1))
print("Лев сидит в клетке № " + str(zoo.index('lark')+1))
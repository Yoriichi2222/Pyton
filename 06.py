#!/usr/bin/env python3
# -*- coding: utf-8 -*-

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

time = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
print('Три песни звучат '  + str(round(time, 2)) + ' минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time = violator_songs_list[1][1] + violator_songs_list[6][1] + violator_songs_list[7][1]
print('А другие три песни звучат '  + str(round(time, 2)) + ' минут')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

# все виды цветов 
print(garden_set)
print(meadow_set)

# растут и там и там
print(garden_set & meadow_set)

# растут в саду, но не растут на лугу
print(garden_set - meadow_set)

# растут на лугу, но не растут в саду
print(meadow_set - garden_set)
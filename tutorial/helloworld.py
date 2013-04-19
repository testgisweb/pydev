# -*- coding: utf-8 -*-
import csv
with open('eggs.csv', 'rb') as csvfile:
    ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
    ...         print ', '.join(row)
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
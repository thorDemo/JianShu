# -*- conding:utf-8 -*-
import os

path = os.path.split(os.path.realpath(__file__))[0]

file = open('%s/templates/JSModel/static/keywords.txt' % path, 'r+', encoding='utf-8')
for lin in file:
    print(lin)
# -*- conding:utf-8 -*-
import os
import datetime
path = os.path.split(os.path.realpath(__file__))[0]
#
# file = open('%s/templates/JSModel/static/keywords.txt' % path, 'r+', encoding='utf-8')
# for lin in file:
#     print(lin)


now = datetime.datetime.today()
d2 = datetime.timedelta(days=1)
d1 = now - d2
print(now.strftime("[%d/%b/%Y:%H:%M:%S"))
print(d1.strftime("[%d/%b/%Y:%H:%M:%S"))

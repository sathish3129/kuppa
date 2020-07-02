"""import DataMart

header = ['empID']

dm = DataMart.CreateTable(header)

print(dm)
"""

test_str = 'Hyderabad(HYD)'

import re
p = re.compile('^.*?\\((.*)?\\).*$')# .match(str(x[0]))group(1)
m = p.match(test_str)


print(m.group(1))


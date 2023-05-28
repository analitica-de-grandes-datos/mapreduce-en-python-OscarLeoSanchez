#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

current_value = None
for line in sys.stdin:
    line = line.strip()
    line = line.rstrip()
    value, key = line.split("\t")
    if value != current_value:
        current_value = value
        print(f'{key},{value}')
    else:
        print(f'{key},{value}')


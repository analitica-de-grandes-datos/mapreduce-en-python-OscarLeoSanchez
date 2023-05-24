#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

# abrir el archivo de entrada
# with open('credit.csv', 'r') as f:
#     for line in f.readlines():
#         line = line.strip()
#         line = line.strip()
#         line = line.split(',')
#         print(f'{line[2].strip()}\t1')

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.strip()
    line = line.split(',')
    print(f'{line[2].strip()}\t1')

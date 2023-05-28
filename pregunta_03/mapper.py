#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.strip()
    line = line.split(',')
    print(f'{line[1].strip()}\t{line[0]}')
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
max_value = 0
# with open('file.txt', 'r', encoding='utf-16') as f:
    # line = f.readlines()
for line in sys.stdin:
    line = line.rstrip()
    line = line.strip()
    key, value = line.split('\t')
    value = int(value)
    if key == current_key:
        if value > max_value:
            max_value = value
    else:
        if current_key is not None:
            print(f'{current_key}\t{max_value}')
        current_key = key
        max_value = value
if current_key is not None:
    print(f'{current_key}\t{max_value}')

#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
current_count = 0
# with open('file.txt', 'r', encoding='utf-16') as f:
    # line = f.readlines()
for line in sys.stdin:
    line = line.rstrip()
    line = line.strip()
    key, value = line.split('\t')
    value = int(value)
    if key == current_key:
        current_count += value

    else:
        if current_key is not None:
            print(f'{current_key}\t{current_count}')
        current_key = key
        current_count = value
if current_key is not None:
    print(f'{current_key}\t{current_count}')

# cat credit.csv | python3 mapper.py | python3 reducer.py
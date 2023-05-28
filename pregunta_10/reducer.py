#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == '__main__':
    current_key = None
    list_values = []
    for line in sys.stdin:
        key, value = line.split("\t")
        value = int(value)
        if key == current_key:
            list_values.append(value)
        else:
            if current_key is not None:
                sys.stdout.write("{}\t{}\n".format(current_key, ','.join(str(i) for i in sorted(list_values))))
            current_key = key
            list_values = []
            list_values.append(value)
        # print(list_values)
    sys.stdout.write("{}\t{}\n".format(current_key, ','.join(str(i) for i in sorted(list_values))))
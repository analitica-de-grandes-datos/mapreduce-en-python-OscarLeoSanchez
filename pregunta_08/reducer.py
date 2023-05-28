#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    current_key = None
    suma = 0
    current_count = 0
    for line in sys.stdin:
        key, val, count = line.split("\t")
        count = int(count)
        val = float(val)
        if key == current_key:
            suma += val
            current_count += count
        else:
            if current_key is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(current_key, suma, suma/current_count))
            current_key = key
            suma = val
            current_count = count
    sys.stdout.write("{}\t{}\t{}\n".format(current_key, suma, suma/current_count))

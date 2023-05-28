#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    current_key = None
    minimo = None
    maximo = None
    for line in sys.stdin:
        key, val = line.split("\t")
        val = float(val)
        if key == current_key:
            if val > maximo:
                maximo = val
            if val < minimo:
                minimo = val
        else:
            if current_key is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(current_key, maximo, minimo))
            current_key = key
            maximo = val
            minimo = val
    sys.stdout.write("{}\t{}\t{}\n".format(current_key, maximo, minimo))
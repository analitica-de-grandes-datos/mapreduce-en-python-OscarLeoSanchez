#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import re

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        splits = re.split("[ ]+", line)
        letra = splits[0]
        fecha = splits[1]
        valor = splits[2]
        sys.stdout.write("{}\t{}\t{}\n".format(letra, fecha, valor))
        # print(splits)
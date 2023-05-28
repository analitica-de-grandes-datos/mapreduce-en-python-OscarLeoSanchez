#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        line = line.strip()
        line = line.split('   ')
        month = line[1].split('-')[1]
        sys.stdout.write("{month}\t1\n".format(month=month))
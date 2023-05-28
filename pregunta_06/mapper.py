#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        line = line.strip()
        line = line.split('   ')
        sys.stdout.write("{line[0]}\t{line[2]}\n".format(line=line))
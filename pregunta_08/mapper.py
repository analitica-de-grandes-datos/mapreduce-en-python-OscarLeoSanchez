#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import re
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        splits = re.split("\s+", line)
        sys.stdout.write("{}\t{}\t1\n".format(splits[0],splits[2]))
            
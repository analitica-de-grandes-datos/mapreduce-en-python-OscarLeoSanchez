#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import re
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        splits = re.split("\t", line)
        
        result = [(splits[0], letter) for letter in splits[1].split(',')]

        for num, letter in result:
            sys.stdout.write("{}\t{}\n".format(letter, num))
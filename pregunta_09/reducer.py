#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    list_values = list()
    for line in sys.stdin:
        line = line.strip()
        letter, date, value = line.split("\t")
        value = int(value)
        list_values.append((letter, date, value))
    list_values.sort(key=lambda x: x[2])
    for i in range(6):
        sys.stdout.write("{}   {}   {}\n".format(list_values[i][0], list_values[i][1], list_values[i][2]))
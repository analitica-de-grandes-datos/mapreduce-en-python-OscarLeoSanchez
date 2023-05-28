#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

# import sys

# if __name__ == '__main__':
#     current_key = None
#     current_date = None
#     current_value = None
#     for line in sys.stdin:
#         key, date, value = line.split("\t")
#         value = float(value)
#         if key == current_key:
#             if value > current_value:
#                 current_value = max(current_value, value)
#             else:
#                 sys.stdout.write("{}\t{}\t{}\n".format(current_key, current_date, current_value))
#                 current_date = date
#                 current_value = value
#         else:
#             if current_key is not None:
#                 sys.stdout.write("{}\t{}\t{}\n".format(current_key, current_date, current_value))
#             current_key = key
#             current_date = date
#             current_value = value
#     sys.stdout.write("{}\t{}\t{}\n".format(current_key, current_date, current_value))
import sys

current_letter = None
values = []

for line in sys.stdin:
    line = line.strip()
    key, date, value = line.split('\t')

    if current_letter is None:
        current_letter = key

    if key == current_letter:
        values.append((date, int(value)))
        
    else:
        if current_letter is not None:
            sorted_values = sorted(values, key=lambda x: x[1])
            for d, v in sorted_values:
                print(f'{current_letter}   {d}   {v}')
            current_letter = key
            values = [(date, int(value))]
        date = date

sorted_values = sorted(values, key=lambda x: x[1])
for date, val in sorted_values:
    print(f'{current_letter}   {date}   {val}')
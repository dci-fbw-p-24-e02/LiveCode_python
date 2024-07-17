import sys 
import getopt

def sum_args(a, b):
    return int(a) + int(b)

args = sys.argv[1:]

output = getopt.getopt(args, 'a:b:', ['Number1=', 'Number2='])
opts = output
print(opts)
#positional
# print(opts[1])
# lst = opts[1]
# a = lst[0]
# b = lst[1]

try: 
    a, b = opts[1]
except ValueError:
    print('Not positional')

lst_1 = opts[0]

# print(list(zip(*lst_1)))
a, b = list(zip(*lst_1))[1]
print(a, b)
# print(lst_1)
# tuple_1 = lst_1[0]
# a = tuple_1[1]
# print(a)
# b = opts[0][1][1]
# print(b)


print(sum_args(a, b))
    
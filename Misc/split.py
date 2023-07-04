from sys import getsizeof

s = ''
a = [3,2,1]

for i in a:
    s += str(i)
print(int(s))

b = ['1','2','3','4']
c = {'6':3}
d = '123456666666666666661000000000000000000000fas0fa0s0fd0as0fdsa0fd0sa0df0as0'

print(getsizeof(b),getsizeof(c), getsizeof(d))
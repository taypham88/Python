
# dominoes = [[1,2],[2,1],[3,4],[5,6]]
# set_d, total = [], []
# sum = 0
# for i in dominoes:
#     set_d.append(set(i))
# for i in set_d:
#     total.append(set_d.count(i))
# tot = list(set(total))
a = [1,2,3,4,5]
for i in a:
    print(i*(i-1)//2)
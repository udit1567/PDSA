V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
AList = {}
# In dictionay AList, for example, AList[i] = [j,k] represent two edge from i to j and i to k
for i in range(size):
    AList[i] = []
for (i,j) in E:
    AList[i].append(j)
print(AList)
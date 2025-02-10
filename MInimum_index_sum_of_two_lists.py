L1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
L2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']

index1 = 10
index2 = 10
for i in range(len(L1)):
    index = L2.index(L1[i])
    if i + index < index1 + index2:
        index1 = i
        index2 = index
print(L1[index],index1 + index2)
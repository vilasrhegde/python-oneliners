from collections import Counter
a=[10, 30, 40, 20, 10, 20, 50, 10] 
rem=set()
for i in a: 
    if a.count(i)>1: 
        rem.add(i)
for i in a:
    if i not in rem:
        print(i,end=' ')
        
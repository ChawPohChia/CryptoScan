x = {'a':1,'b':4,'c':2}
a={k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
print(a)

for item in a:
   print(item+":"+str(a[item]))

#hisPrice=[1,2,3,4,5,0,9,9,9]

#for i in hisPrice:
#    if (i == 0):
#        continue;
#    print(i)
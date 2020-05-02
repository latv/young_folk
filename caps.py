cap1 =	['F','F','B','H','B','F','B','B','B','F','H','F','F']
cap2 = []

capF =[]

capB = []
for i in range(len(cap1)):
    # if i == 0:
    #     cap2+=cap1[i]
    #     continue
    # if cap1[i-1] == cap1[i]:
    #     cap2+=cap1[i]
    # if cap1[i-1] != cap1[i]:
    #     cap2+=cap1[i]
    if i == 0:
        cap2+=[i]
        continue
    if cap1[i-1] != cap1[i]:
        cap2+=[i]


print(cap2)


for i in range(len(cap2)):
    if i == 0:
        continue
    if i%2 == 0:
        capB+=[cap2[i]-cap2[i-1]]
    if i%2 != 0:
        capF+=[cap2[i]-cap2[i-1]]
print("capB: ",capB)
print("capF: ",capF)
capBTotal=0
for i in capB:
    capBTotal+=i
capFTotal=0
for i in capF:
    capFTotal+=i
print("capBTotal: ",capBTotal)
print("capFTotal: ",capFTotal)

reservedI=0

needToFlip=[]

if (capBTotal>capFTotal):
    for i in range(len(cap1)):
        if (cap1[i]=='B'):
            needToFlip+=[i]
if (capBTotal<capFTotal):
    for i in range(len(cap1)):
        if (cap1[i]=='F'):
            needToFlip+=[i]


print("needToFlip: ",needToFlip)
for i in range(len(needToFlip)):
    if (i == 0 ):
        continue
    if (i==len(needToFlip)-1):
        print("flip ",needToFlip[i])
        break
    if (needToFlip[i]+1==needToFlip[i+1]):
        print ("flip ",needToFlip[i] )



# for i in range(len(cap2)):
#     if i%2 == 0:
#         capB+=[cap2[i]]
#     if i%2 != 0:
#         capF+=[cap2[i]]
# print("capB: ",capB)
# print("capF: ",capF)




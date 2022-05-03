dic1Ex1 = {5: ['Panera'], 10: ['RedSeven', 'BK']}
dic2Ex1 = {10: ['Heisei', 'Panera'], 20: ['BK']}
list1 = []
list2 = []
list3 = []
for i in dic1Ex2:
    if i < 15:
        list1.append(dic1Ex2[i])
        
for x in dic2Ex2:
    if x < 15:
        list1.append(dic2Ex2[i])

for sublist in list1:
    for i in sublist:
        list2.append(i)

for i in range(len(list2)):
    for x in range(i+1, len(list2)):
        if list2[i] == list2[x]:
            list3.append(list2[i])
    
set = set(list3)
print(set)
nameList=input('camelcase:  ')

for i in nameList:
    if i.isupper():
        nameList=nameList.replace(i,'_'+i.lower())
print(nameList)

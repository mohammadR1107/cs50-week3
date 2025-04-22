list = input("input:  ")

for i in list:
    if i=='a'or i=='A':
        list=list.replace(i,"")
    elif i=='e' or i=='E':
        list=list.replace(i,"")
    elif i=='i' or i=='I':
        list=list.replace(i,"")
    elif i=='o' or i=='O':
        list=list.replace(i,'')
    elif i=='u'or i=='U':
        list=list.replace(i,'')
print("output:",list)
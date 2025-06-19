#Name Analyzer

name = input("enter your name: ")
print(name)
print("legth if name:" , len(name))
print("first letter" , name[0])
print("last letter" , name[-1])
print("Name in uppercase: " , name.upper())
print("Name in lowercase: ", name.lower())
print("reversed name" , name[::-1])

if ('a' in name.lower()):
    print("Does name contain 'a'? YES")
else:
    print("Does name contain 'a'? No")
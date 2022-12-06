var1 = 6
var2 = 4
var3 = int(input("Num dalo "))

if var3 > var2:
    print("var3 greater")
elif var1>var2:
    print("ouch")
else:
    print("tada")

#! Another application of 'if'
list1 = [5,7,8,9]
if 5 in list1:
    print("5 Ache")

print(15 in list1) # Will return bool
print(15 not in list1) # Will return bool

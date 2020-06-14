# 1. code begins
print("Geeks for Geeks")

x=1000000000000
x=x+1
print(x)

a="Geeks for geeks"
b=3
print(type(a))
print(type(b))

print(10**10)
print(4**2)

a='geeks'
b=' for'
c=' geeks'
print(a+b+c)


# 2.
a=3
A=2
print(a+A)
print(a-A)
print(a/A)
print(a//A)
print(a*A)
print(a**A)

# Check the condition of odd and even
a=36
if a%2==0:
    print("Even")
else:
    print("odd")

# Or
a=36
if a%2==0:
    print("even")
elif a%2!=0:
    print("odd")

# Declare a Function
def checkoddoreven(a):
    if a%2==0:
        print("Even")
    elif a%2!=0:
        print("Odd")
checkoddoreven(52)

# 3.
# String: Immutable (The value does not changed once declared)
a='Python in geeksforgeeks'
print(a)

# Lists: Mutable (The value can be changed)
lists=[6,'geeksforgeeks',10]
print(lists)
print(lists[1])

# Tupple: Immutable (same as lists but it is immutable means it cannot be changed once declared)
tup=(6,"rahul",55,25.32)
print(tup)
print(tup[2])
print(type(tup))

# Iteration by while loop
i=0
while i<10:
    i=i+1
    print(i)

b="Hello World"
for i in b:
    print(i)

c=[1,2,3,4,5,6,7]
for i in c:
    print(i)

for i in range(0,10):
    print(i)

# 4.
a="Rahul mondal"
print(len(a))

a="This is a python tutorial"
print(a.count("is",0,len(a)))

str="Geeksforgeeks"
print(str.center(100,'-'))
print(str.ljust(100,'-'))
print(str.rjust(100,'-'))

str1='abc'
str2='abc23'
str3='     '
print("for string1:isalpha()-->",str1.isalpha())
print("for string1:isalnum()-->",str1.isalnum())
print("for string1:isspace()-->",str1.isspace())
print()
print("for string2:isalpha()-->",str2.isalpha())
print("for string2:isalnum()-->",str2.isalnum())
print("for string2:isspace()-->",str2.isspace())
print("for string3:isalpha()-->",str3.isalpha())
print("for string3:isalnum()-->",str3.isalnum())
print("for string3:isspace()-->",str3.isspace())

l=["geeks","for","geeks"]
s="_"
print(s.join(l))


# 5.
str="This is a python tutorial"
#print("The first occurence of 'is' is at:")
print(str.find("is",0,len(str)))
print(str.rfind("is",0,len(str)))


# 6.
str="------geeksforgeeks------"
print(str.strip('-'))
print(str.lstrip('-'))
print(str.rstrip('-'))

str="geeks"
greeting = "morning"

if greeting == "morning":
   print("Good morning")
else:
    print("Good afternoon")
print("*******************************")

#####Looops
obj=[2,3,4,5,6,7]

for num in obj:
    print(num)
print("*******************************")

###Print the list with multiples of 2
for i in range(1,11):
    print(i * 2)
print("*******************************")
#Sum of first natural numbers
addition=0
for j in range(1,6):
    addition+=j
print(addition)

print("*******************************")
#Display numbers in difference of 2
for j in range(2,11,2):
    print(j)

print("*******************************")
#### Create a dictionary at runtime and add values
dict={}
dict["name"] = "Smita"
dict["age"] = 25
print(dict)


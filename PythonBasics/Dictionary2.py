Dictionary={'Alice':'Dec 12','Bob':'Sep 14','Charlie':'Sep 15'}

for key in Dictionary.keys():
    print(key)

for values in Dictionary.values():
    print(values)

for item in Dictionary.items():
    print(item)

for k,v in Dictionary.items():
    print(f"Key is :{k} Value is :{v}")

print(f"My birthday is on {Dictionary['Alice']}")

if 'Smita' not in Dictionary:
    Dictionary['Smita']='Sep 5'
print(Dictionary)

# Set the Default value to the key item if the key is not exist
Dictionary.setdefault("Dhruv","May 30")
print(Dictionary)
Dictionary.setdefault("Dhruv","May 29")  ###not changing value setting default value
print(Dictionary)

Dictionary.setdefault("Vinod","April 16")
print(Dictionary)


# Print the number of occurrences of each letter in the string by using setdefault()
Message="I love my country India"
Count={}

for char in Message:
    Count.setdefault(char,0)
    Count[char]+=1

print(Count)











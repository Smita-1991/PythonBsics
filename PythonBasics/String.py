str="RahulShettyAcademy.com"
str1="Hello"
str3="com"
print(str)
print(str[0:18])   ##RahulShettyAcademy

print("{},{}".format(str1,str)) ### Concatenation
print(str3 in str)   #### Substring check

var=str.split(".")   #### Splitting the string
print(var)
print(var[1])

####Remove the front and end white spaces
str4="   str   "
print(str4.strip())
print(str4.lstrip()) #####Remove the left spaces
print(str4.rstrip()) #####Remove the right spaces





values=[1,"Smita","Novi",48375]
#List is a datatype which allow to store multiple values of different datatype

print(values)
#[1, 'Smita', 'Novi', 48375]

print(values[0])
#1

print(values[-1])
#48375

print(values[0:2])
#[1, 'Smita']

values.insert(4,"Vinod")
print(values)
#[1, 'Smita', 'Novi', 48375, 'Vinod']

values.pop(2)
print(values)
#[1, 'Smita', 48375, 'Vinod']

values[2]="Michigan"
print(values)

del values[2]
print(values)


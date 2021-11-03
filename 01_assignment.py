#Shane
#Assignment Examples

#You can assign "values" to "variables" by using an equals(right side goes into left side)
x=5

#When python reads a variable name, it replaces it with the variable's stored value
y=x+5

#There are four different primitive datatypes
#Integers: any whole number, positive or negative 
age=15
#Float: any number with a decimal, positive or negative
grade=98.6
#String: a string of human-readable characters 
name="Shane"
#Numbers in a string are not numbers, they are letters
favoriteNumber="69"
#Boolean: True or False
#True is any value that is not False or empty
isSmart=True

#You can output to the console by using 'print()'
print(name)
print(grade)
print(age)
print(favoriteNumber)
print(isSmart)

#You can concatenate similar values together
print("My name is " + name)
#You can use funtions to convert datatypes
print("and my age is " + str(age))
#Don't forget! If you want to convert a value permanently you must assign the converted value to a variable
age=str(age)
#You can convert back and forth with int(), str(), bool(), and float()
print(int(age))
print(float(age))
print(bool(age))

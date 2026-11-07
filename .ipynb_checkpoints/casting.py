print("\n1. STRING TO INTEGER")

num = "100"

print("Before Conversion:", num)
print("Before Type:", type(num))

num = int(num)

print("After Conversion:", num)
print("After Type:", type(num))
print("Addition:", num + 50)


print("\n2. INTEGER TO FLOAT")

num = 25

print("Before Conversion:", num)
print("Before Type:", type(num))

num = float(num)

print("After Conversion:", num)
print("After Type:", type(num))



print("\n3. INTEGER TO STRING")

age = 21

print("Before Conversion:", age)
print("Before Type:", type(age))

age = str(age)

print("After Conversion:", age)
print("After Type:", type(age))

print("My age is " + age)


# EXAMPLE 4: FLOAT TO INTEGER

print("\n4. FLOAT TO INTEGER")

price = 99.99

print("Before Conversion:", price)
print("Before Type:", type(price))

price = int(price)

print("After Conversion:", price)
print("After Type:", type(price))



print("\n5. STRING TO FLOAT")

salary = "25000.50"

print("Before Conversion:", salary)
print("Before Type:", type(salary))

salary = float(salary)

print("After Conversion:", salary)
print("After Type:", type(salary))

bonus = salary + 5000

print("Total Salary:", bonus)

student_name = input("Enter your name: ")
mark = int(input("Enter your mark: "))

if 90 <= mark <= 100:
    print(f"{student_name} got A+ grade")
elif 80 <= mark <= 89:
    print(f"{student_name} got A grade")
elif 70 <= mark <= 79:
    print(f"{student_name} got B grade")
elif 60 <= mark <= 69:
    print(f"{student_name} got C grade")
elif 50 <= mark <= 59:
    print(f"{student_name} got D grade")
elif 35 <= mark <= 49:
    print(f"{student_name} got E grade")
elif 0 <= mark < 35:
    print(f"{student_name} got Fail")
else:
    print("enter vaild input")
    
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >=60:
   print(f"{name}'s age is {age}. The ticket price for {name} is 120 rupees.")
elif  18<= age <=59:
     print(f"{name}'s age is {age}. The ticket price for {name} is 200 rupees.")
elif  13<= age <=17:
     print(f"{name}'s age is {age}. The ticket price for {name} is 150 rupees.")     
elif   5<= age <=12:
     print(f"{name}'s age is {age}. The ticket price for {name} is 100 rupees.")       
elif  0<= age <5:
     print(f"{name}'s age is {age}. The ticket price for {name} is free.")      
else:
    print("enter vaild input")
         
account_balance=int(input("Enter your account balance amount : "))
withdrawal_ammount=int(input("Enter your account withdrawal amount : ") )       
if withdrawal_ammount <= 0 :
    print(f"kindly enter amount greater than 0")
elif withdrawal_ammount % 100 != 0 :
     print(f"kindly enter amount which is multiples of ₹100")
elif withdrawal_ammount > balance:
    print("Insufficient balance.")     
else :
      print(f"your account has {account_balance-withdrawal_ammount} remaning")
      remaining_balance = account_balance - withdrawal_ammount
      print(f"Withdrawal successful.")
      print(f"Remaining balance: ₹{remaining_balance}")
      
unit_used=float(input("Enter unit that used in this month : ")
if unit_used > 500:
    print(f"This month's electricity bill is {unit_used * 8}")
elif 201 <= unit_used <= 500:
    print(f"This month's electricity bill is  {unit_used * 5}")
elif 101 <= unit_used <= 200:
    print(f"This month's electricity bill is  {unit_used * 3}")
elif 0 <= unit_used <= 100:
    print(f"This month's electricity bill is  {unit_used * 2}")
else:
    print("Enter a valid input")
    
user=(input("Enter your username : "))
pas=(input("Enter your password : "))
username="admin"
password="admin123"
if pas == password and  user == username:
    print(f"Login Successful")
else:
      print("Invalid Username and Incorrect Password.")  
        
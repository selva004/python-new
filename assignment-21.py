{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4b528f5a-a827-43f6-adfa-b5c657618b2f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  selva\n",
      "Enter your mark:  88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "selva got A grade\n"
     ]
    }
   ],
   "source": [
    "student_name = input(\"Enter your name: \")\n",
    "mark = int(input(\"Enter your mark: \"))\n",
    "\n",
    "if 90 <= mark <= 100:\n",
    "    print(f\"{student_name} got A+ grade\")\n",
    "elif 80 <= mark <= 89:\n",
    "    print(f\"{student_name} got A grade\")\n",
    "elif 70 <= mark <= 79:\n",
    "    print(f\"{student_name} got B grade\")\n",
    "elif 60 <= mark <= 69:\n",
    "    print(f\"{student_name} got C grade\")\n",
    "elif 50 <= mark <= 59:\n",
    "    print(f\"{student_name} got D grade\")\n",
    "elif 35 <= mark <= 49:\n",
    "    print(f\"{student_name} got E grade\")\n",
    "elif 0 <= mark < 35:\n",
    "    print(f\"{student_name} got Fail\")\n",
    "else:\n",
    "    print(\"enter vaild input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "395bf3fa-3036-47c4-915b-452af967223c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  siva\n",
      "Enter your age:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "siva's age is 3. The ticket price for siva is free.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "age = int(input(\"Enter your age: \"))\n",
    "if age >=60:\n",
    "   print(f\"{name}'s age is {age}. The ticket price for {name} is 120 rupees.\")\n",
    "elif  18<= age <=59:\n",
    "     print(f\"{name}'s age is {age}. The ticket price for {name} is 200 rupees.\")\n",
    "elif  13<= age <=17:\n",
    "     print(f\"{name}'s age is {age}. The ticket price for {name} is 150 rupees.\")     \n",
    "elif   5<= age <=12:\n",
    "     print(f\"{name}'s age is {age}. The ticket price for {name} is 100 rupees.\")       \n",
    "elif  0<= age <5:\n",
    "     print(f\"{name}'s age is {age}. The ticket price for {name} is free.\")      \n",
    "else:\n",
    "    print(\"enter vaild input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "cf4e1c7c-c08d-4354-ad27-43f7885c0ace",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your account balance amount :  1000\n",
      "Enter your account withdrawal amount :  500\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "your account has 500 remaning\n",
      "Withdrawal successful.\n",
      "Remaining balance: 500\n"
     ]
    }
   ],
   "source": [
    "account_balance=int(input(\"Enter your account balance amount : \"))\n",
    "withdrawal_ammount=int(input(\"Enter your account withdrawal amount : \") )       \n",
    "if withdrawal_ammount <= 0 :\n",
    "    print(f\"kindly enter amount greater than 0\")\n",
    "elif withdrawal_ammount % 100 != 0 :\n",
    "     print(f\"kindly enter amount which is multiples of ₹100\")\n",
    "elif withdrawal_ammount > account_balance:\n",
    "    print(\"Insufficient balance.\")     \n",
    "else :\n",
    "      print(f\"your account has {account_balance-withdrawal_ammount} remaning\")\n",
    "      remaining_balance = account_balance - withdrawal_ammount\n",
    "      print(f\"Withdrawal successful.\")\n",
    "      print(f\"Remaining balance: {remaining_balance}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "afcfbe77-6ba7-40bb-8fd1-32f06a56a7c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter units used this month:  200\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This month's electricity bill is  600.0\n"
     ]
    }
   ],
   "source": [
    "unit_used = float(input(\"Enter units used this month: \"))\n",
    "\n",
    "if unit_used > 500:\n",
    "    print(f\"This month's electricity bill is {unit_used * 8}\")\n",
    "elif 201 <= unit_used <= 500:\n",
    "    print(f\"This month's electricity bill is  {unit_used * 5}\")\n",
    "elif 101 <= unit_used <= 200:\n",
    "    print(f\"This month's electricity bill is  {unit_used * 3}\")\n",
    "elif 0 <= unit_used <= 100:\n",
    "    print(f\"This month's electricity bill is  {unit_used * 2}\")\n",
    "else:\n",
    "    print(\"Enter a valid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "ed71f373-f9d6-4f6b-8b99-5f071d826e25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your username :  admin\n",
      "Enter your password :  ksphdav\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid Username and Incorrect Password.\n"
     ]
    }
   ],
   "source": [
    "user=(input(\"Enter your username : \"))\n",
    "pas=(input(\"Enter your password : \"))\n",
    "username=\"admin\"\n",
    "password=\"admin123\"\n",
    "if pas == password and  user == username:\n",
    "    print(f\"Login Successful\")\n",
    "else:\n",
    "      print(\"Invalid Username and Incorrect Password.\")               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7ee98b54-cc82-4a48-9aac-2ca3a8cf2af4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  ram\n",
      "Enter your salary:  15000\n",
      "Enter your rating (1 - 5):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram got 10% bonus. Bonus amount is 1500.0, actual salary is 15000, and salary after bonus is 16500.0.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "salary = int(input(\"Enter your salary: \"))\n",
    "rating = int(input(\"Enter your rating (1 - 5): \"))\n",
    "\n",
    "if rating < 1 or rating > 5:\n",
    "    print(\"Enter rating between 1 to 5 only\")\n",
    "else:\n",
    "    if rating == 5:\n",
    "        bonus_percent = 20\n",
    "        bonus = salary * 0.20\n",
    "    elif rating == 4:\n",
    "        bonus_percent = 15\n",
    "        bonus = salary * 0.15\n",
    "    elif rating == 3:\n",
    "        bonus_percent = 10\n",
    "        bonus = salary * 0.10\n",
    "    elif rating == 2:\n",
    "        bonus_percent = 5\n",
    "        bonus = salary * 0.05\n",
    "    elif rating == 1:\n",
    "        bonus_percent = 0\n",
    "        bonus = 0\n",
    "\n",
    "    total_salary = salary + bonus\n",
    "\n",
    "    if bonus > 0:\n",
    "        print(f\"{name} got {bonus_percent}% bonus. Bonus amount is {bonus}, actual salary is {salary}, and salary after bonus is {total_salary}.\")\n",
    "    else:\n",
    "        print(f\"{name} got no bonus and actual salary is {salary}.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "d3796e1f-9a88-49d0-a82e-bbf84ebaeb03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your order amount:  22222\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your purchased amount is 22222. Discount amount you got is 4444.400000000001 and final price you bought is 17777.6.\n"
     ]
    }
   ],
   "source": [
    "order_amount = int(input(\"Enter your order amount: \"))\n",
    "\n",
    "if order_amount >= 20000:\n",
    "    discount = order_amount * 0.20\n",
    "elif 10000 <= order_amount <= 19999:\n",
    "    discount = order_amount * 0.15\n",
    "elif 5000 <= order_amount <= 9999:\n",
    "    discount = order_amount * 0.10\n",
    "elif 1000 <= order_amount <= 4999:\n",
    "    discount = order_amount * 0.05\n",
    "else:\n",
    "    discount = 0\n",
    "\n",
    "total_amount = order_amount - discount\n",
    "\n",
    "if discount > 0:\n",
    "    print(f\"Your purchased amount is {order_amount}. Discount amount you got is {discount} and final price you bought is {total_amount}.\")\n",
    "else:\n",
    "    print(f\"You got no discount and your purchased amount is {order_amount}.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c4f9710d-f890-4fff-8b66-a81784ecba35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the distance you covered so far :  655\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You covered distance of 655 and fare is 5240.\n"
     ]
    }
   ],
   "source": [
    "distance=int(input(\"Enter the distance you covered so far : \"))\n",
    "if distance > 30:\n",
    "    fare = distance * 8\n",
    "    print(f\"You covered distance of {distance} and fare is {fare}.\")  \n",
    "elif 16 <= distance <= 30:\n",
    "    fare =distance * 10\n",
    "    print(f\"You covered distance of {distance} and fare is {fare}.\")\n",
    "elif 6 <= distance <= 15:\n",
    "    fare = distance * 12\n",
    "    print(f\"You covered distance of {distance} and fare is {fare}.\")\n",
    "elif 0 <= distance <= 5:\n",
    "    fare = 50\n",
    "    print(f\"You covered distance of {distance} and fare is {fare}.\")\n",
    "else:\n",
    "    print(\"Enter only postive input \")    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cb81f69-646f-4b0e-9999-d5769ff123bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

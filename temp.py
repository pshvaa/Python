# -*- coding: utf-8 -*-
# CALCULATOR

print("Operation: +, -, *, /")
try:
  while True:
    oper = input("Please enter operation: ")
    if oper in ("+","-","*","/"):
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))

       if oper == "+":
            print(num1, "+", num2, "=", num1+num2)
       
       elif oper == "-":
            print(num1, "-", num2, "=", num1-num2)

       elif oper == "*":
            print(num1, "*", num2, "=", num1*num2)
       
       elif oper == "/":
            print(num1, "/", num2, "=", num1/num2)
    
       ques = input("Do you want to continue?(yes/no): ")
       if ques == "no":
           break
    else:
       print("Please enter valid operation.")
except ValueError:
    print("Just enter a number!!")
except ZeroDivisionError:
    print("Can't divide by zero!!")
    
    
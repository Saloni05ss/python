#simple calculator which can perform between two operands
#It can do addition, subtraction, multiplication, division which will give decimal value, quotient, remainder, exponential value
print("select an operation to perform")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division to get value in decimal form")
print("5.division to get quotient")
print("6.division to get remainder")
print("7.exponential value")

operation=input()

if operation == "1":
    a=input("enter first number:")
    b=input("enter second number:")
    print("The addition result is="+ str(int(a)+int(b)))
elif operation == '2':
    a=input("enter first number:")
    b=input("enter second number:")
    print("The subtraction result is="+ str(int(a)-int(b)))
elif operation == '3':
    a=input("enter first number:")
    b=input("enter second number:")
    print("The multiplication result is="+ str(int(a)*int(b)))
elif operation == '4':
    a=input("enter first number:")
    b=input("enter second number:")
    print("The division result is="+ str(int(a)/int(b)))
elif operation == '5':
    a=input("enter first number:")
    b=input("enter second number:")
    print("The quotient is="+ str(int(a)//int(b)))
elif operation == '6':
    a=input("enter first number:")
    b=input("enter second number:")
    print("The remainder is="+ str(int(a)%int(b)))
elif operation == '7':
    a=input("enter base number:")
    b=input("enter exponent number:")
    print("The first_num^second_num result is="+ str(int(a)**float(b)))
else:
    print("invalid entry.....")
#here the input values must be string type so written within double quote
#also we take input string, make it integer then addition takes place then again make it string that displayed in output

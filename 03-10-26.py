# print("connnection established : ")
# try:
#     p=int(input("enter the principle amount : "))
#     t=int(input("enter the time in years : "))
#     r=float(input("enter the rate of interest : "))
#     si=(p*t*r)/100
#     print("the simple interest is : ",si)
# except :
#     print("Invalid input! Please enter numeric values for principle, time, and rate.")



# """Traceback (most recent call last):
#   File "C:\Users\Sunkeerth\Desktop\Sunkeerth_python_prac\03-10-26.py", line 3, in <module>
#     t=int(input("enter the time in years : "))
# ValueError: invalid literal for int() with base 10: 'se' 

# we need when user enter the string insted of integer or the float number . 

# so use the  
# "try and except block to handle the error and display a message to the user.
# """*/


def execption_handling():
    # Inputs are now inside the try block to catch ValueError
    try:
        num1=int(input("enter the first number : "))
        num2=int(input("enter the second number : "))
    
        res=num1/num2
        # print(res)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")
        raise e  # Re-raise the exception to propagate it further if needed
    finally:
        print("Execution completed.")
        
try:
    execption_handling()
except ZeroDivisionError as e1:
    print("cauget the error at the function level and raised to the main function : ", e1)
    
    
